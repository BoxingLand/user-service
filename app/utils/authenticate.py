import grpc

from app.crud.user import get_user_by_email, get_user_by_phone_number
from app.models.user import User
from app.user import user_pb2
from app.utils.password import verify_password


async def authenticate(
        signin_data: user_pb2.SigninRequest,
        context: grpc.aio.ServicerContext,

) -> User | None:
    user: User
    if signin_data.email != "":
        user = await get_user_by_email(email=signin_data.email)
        if user is None:
            await context.abort(grpc.StatusCode.NOT_FOUND)
    elif signin_data.phone_number != "":
        user = await get_user_by_phone_number(phone_number=signin_data.phone_number)
        if user is None:
            await context.abort(grpc.StatusCode.NOT_FOUND)
    else:
        ...

    if not verify_password(signin_data.password, user.password):
        await context.abort(grpc.StatusCode.INVALID_ARGUMENT, details="WrongPassword")

    return user