
from timeit import default_timer
from typing import Awaitable, Callable
import grpc
from loguru import logger

from prometheus_client.registry import REGISTRY
from py_grpc_prometheus import grpc_utils
from py_grpc_prometheus import server_metrics


LEGACY = True
SKIP_EXCEPTION = False
ENABLE_HANDLING_TIME_HISTOGRAM = True

_code_to_status_mapping = {x.value[0]: x for x in grpc.StatusCode}

metrics = server_metrics.init_metrics(REGISTRY)
grpc_server_handled_total_counter = server_metrics.get_grpc_server_handled_counter(
    LEGACY,
    REGISTRY,
)



async def _wrap_async_iterator_inc_counter(iterator, counter, grpc_type, grpc_service_name, grpc_method_name):
    async for item in iterator:
        counter.labels(
            grpc_type=grpc_type,
            grpc_service=grpc_service_name,
            grpc_method=grpc_method_name).inc()
        yield item


def _compute_error_code(grpc_exception):
    if isinstance(grpc_exception, grpc.aio.Call):
        return grpc_exception.code()
    return grpc.StatusCode.UNKNOWN


def _compute_status_code(servicer_context):
    if servicer_context.code() is None:
        return grpc.StatusCode.OK
    return _code_to_status_mapping[servicer_context.code()]


def _increase_grpc_server_started_counter(grpc_type, grpc_service_name, grpc_method_name):
    metrics["grpc_server_started_counter"].labels(
        grpc_type=grpc_type,
        grpc_service=grpc_service_name,
        grpc_method=grpc_method_name
    ).inc()


def _increase_grpc_server_handled_total_counter(grpc_type, grpc_service_name, grpc_method_name, grpc_code):
    if LEGACY:
        grpc_server_handled_total_counter.labels(
            grpc_type=grpc_type,
            grpc_service=grpc_service_name,
            grpc_method=grpc_method_name,
            code=grpc_code
        ).inc()
    else:
        grpc_server_handled_total_counter.labels(
            grpc_type=grpc_type,
            grpc_service=grpc_service_name,
            grpc_method=grpc_method_name,
            grpc_code=grpc_code
        ).inc()


def _increase_grpc_server_handled_latency(grpc_type, grpc_service_name, grpc_method_name, start):
    if LEGACY:
        metrics["legacy_grpc_server_handled_latency_seconds"].labels(
            grpc_type=grpc_type,
            grpc_service=grpc_service_name,
            grpc_method=grpc_method_name
        ).observe(max(default_timer() - start, 0))
    elif ENABLE_HANDLING_TIME_HISTOGRAM:
        metrics["grpc_server_handled_histogram"].labels(
            grpc_type=grpc_type,
            grpc_service=grpc_service_name,
            grpc_method=grpc_method_name
        ).observe(max(default_timer() - start, 0))


def _wrap_rpc_behavior(handler, new_behavior_factory, grpc_service_name, grpc_method_name):
    """Returns a new rpc handler that wraps the given function"""
    if handler is None:
        return None

    if handler.request_streaming and handler.response_streaming:
        orig_behavior = handler.stream_stream
        handler_factory = grpc.stream_stream_rpc_method_handler
    elif handler.request_streaming and not handler.response_streaming:
        orig_behavior = handler.stream_unary
        handler_factory = grpc.stream_unary_rpc_method_handler
    elif not handler.request_streaming and handler.response_streaming:
        orig_behavior = handler.unary_stream
        handler_factory = grpc.unary_stream_rpc_method_handler
    else:
        orig_behavior = handler.unary_unary
        handler_factory = grpc.unary_unary_rpc_method_handler

    return handler_factory(
        behavior=new_behavior_factory(orig_behavior,
                                      handler.request_streaming,
                                      handler.response_streaming,
                                      grpc_service_name,
                                      grpc_method_name),
        request_deserializer=handler.request_deserializer,
        response_serializer=handler.response_serializer,
    )


# ----------------------------------- metrics wrapper

def metrics_wrapper(behavior, request_streaming, response_streaming, grpc_service_name, grpc_method_name):
    async def new_unary_behavior(request_or_iterator, servicer_context):
        response = None
        try:
            start = default_timer()
            grpc_type = grpc_utils.get_method_type(request_streaming, response_streaming)
            try:
                _increase_grpc_server_started_counter(grpc_type, grpc_service_name, grpc_method_name)

                # Invoke the original rpc behavior.
                response = await behavior(request_or_iterator, servicer_context)

                _increase_grpc_server_handled_total_counter(
                    grpc_type,
                    grpc_service_name,
                    grpc_method_name,
                    _compute_status_code(servicer_context).name
                )

                return response

            except grpc.RpcError as exc:
                _increase_grpc_server_handled_total_counter(
                    grpc_type,
                    grpc_service_name,
                    grpc_method_name,
                    _compute_error_code(exc).name
                )
                raise exc

            finally:
                _increase_grpc_server_handled_latency(grpc_type, grpc_service_name, grpc_method_name, start)

        except Exception as exc:  # pylint: disable=broad-except
            # Allow user to skip the exceptions in order to maintain
            # the basic functionality in the server
            # in order to suppress the noise in logging
            logger.error(exc)
            if SKIP_EXCEPTION:
                response = await behavior(request_or_iterator, servicer_context)
                return response
            raise exc

    async def new_stream_behavior(request_or_iterator, servicer_context):
        iterator = None
        try:
            start = default_timer()
            grpc_type = grpc_utils.get_method_type(request_streaming, response_streaming)
            try:
                _increase_grpc_server_started_counter(grpc_type, grpc_service_name, grpc_method_name)

                iterator = _wrap_async_iterator_inc_counter(
                    behavior(request_or_iterator, servicer_context),
                    metrics["grpc_server_stream_msg_sent"],
                    grpc_type,
                    grpc_service_name,
                    grpc_method_name
                )

                async for obj in iterator:
                    yield obj

                _increase_grpc_server_handled_total_counter(
                    grpc_type,
                    grpc_service_name,
                    grpc_method_name,
                    _compute_status_code(servicer_context).name
                )

            except grpc.RpcError as exc:
                _increase_grpc_server_handled_total_counter(
                    grpc_type,
                    grpc_service_name,
                    grpc_method_name,
                    _compute_error_code(exc).name
                )
                raise exc

            finally:
                _increase_grpc_server_handled_latency(grpc_type, grpc_service_name, grpc_method_name, start)

        except Exception as exc:
            logger.error(exc)
            if SKIP_EXCEPTION:
                async for obj in behavior(request_or_iterator, servicer_context):
                    yield obj
            raise exc

    if response_streaming:
        return new_stream_behavior
    return new_unary_behavior


class PromAioServerInterceptor(grpc.aio.ServerInterceptor):
    def __init__(self):
        logger.info("Initializing metric interceptor")

    async def intercept_service(
            self,
            continuation: Callable[[grpc.HandlerCallDetails], Awaitable[grpc.RpcMethodHandler]],
            handler_call_details: grpc.HandlerCallDetails
    ) -> grpc.RpcMethodHandler:
        """
        Intercepts the server function calls.
        Only intercepts unary requests.
        """
        grpc_service_name, grpc_method_name, _ = grpc_utils.split_method_call(handler_call_details)
        handler = await continuation(handler_call_details)
        handler = _wrap_rpc_behavior(handler, metrics_wrapper, grpc_service_name, grpc_method_name)
        return handler
