import abc

import grpc
from loguru import logger

from app.error.error_details import EMAIL, PHONE, NO_SIGNUP_DATA, USER_NOT_FOUND, WRONG_PASSWORD


class Error(abc.ABC):

    @abc.abstractmethod
    async def raise_error(self, context: grpc.aio.ServicerContext):
        """ """


class UserEmailExistError(Error):
    async def raise_error(self, context: grpc.aio.ServicerContext):
        logger.error(f"Status: {grpc.StatusCode.ALREADY_EXISTS}, Details: {EMAIL}")
        await context.abort(code=grpc.StatusCode.ALREADY_EXISTS, details=EMAIL)


class UserPhoneExistError(Error):
    async def raise_error(self, context: grpc.aio.ServicerContext):
        logger.error(f"Status: {grpc.StatusCode.ALREADY_EXISTS}, Details: {PHONE}")
        await context.abort(code=grpc.StatusCode.ALREADY_EXISTS, details=PHONE)


class PasswordNotMatchError(Error):
    async def raise_error(self, context: grpc.aio.ServicerContext):
        logger.error(f"Status: {grpc.StatusCode.INVALID_ARGUMENT}, Details: {PHONE}")
        await context.abort(code=grpc.StatusCode.INVALID_ARGUMENT, details=PHONE)


class WrongPasswordError(Error):
    async def raise_error(self, context: grpc.aio.ServicerContext):
        logger.error(f"Status: {grpc.StatusCode.INVALID_ARGUMENT}, Details: {WRONG_PASSWORD}")
        await context.abort(code=grpc.StatusCode.INVALID_ARGUMENT, details=WRONG_PASSWORD)


class NoSignupDataError(Error):
    async def raise_error(self, context: grpc.aio.ServicerContext):
        logger.error(f"Status: {grpc.StatusCode.INVALID_ARGUMENT}, Details: {NO_SIGNUP_DATA}")
        await context.abort(code=grpc.StatusCode.INVALID_ARGUMENT, details=NO_SIGNUP_DATA)


class UserNotFoundError(Error):
    async def raise_error(self, context: grpc.aio.ServicerContext):
        logger.error(f"Status: {grpc.StatusCode.NOT_FOUND}, Details: {USER_NOT_FOUND}")
        await context.abort(code=grpc.StatusCode.NOT_FOUND, details=USER_NOT_FOUND)


class BoxerProfileNotFoundError(Error):
    async def raise_error(self, context: grpc.aio.ServicerContext):
        logger.error(f"Status: {grpc.StatusCode.NOT_FOUND}")
        await context.abort(code=grpc.StatusCode.NOT_FOUND)


class RoleAlreadyExistsError(Error):
    async def raise_error(self, context: grpc.aio.ServicerContext):
        logger.error(f"Status: {grpc.StatusCode.ALREADY_EXISTS}")
        await context.abort(grpc.StatusCode.ALREADY_EXISTS)
