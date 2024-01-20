from app.crud.user import get_user_by_email, get_user_by_phone_number
from app.exceptions.user_errors import UserNotFoundException, UserValidateException
from app.models.user import User
from app.user import user_pb2
from app.utils.password import verify_password


async def authenticate(
        signin_data: user_pb2.SigninRequest,
) -> User | None:
    user: User
    if signin_data.email is not None:
        user = await get_user_by_email(email=signin_data.email)
        if user is None:
            raise UserNotFoundException()
    elif signin_data.phone_number is not None:
        user = await get_user_by_phone_number(phone_number=signin_data.phone_number)
        if user is None:
            raise UserNotFoundException()
    else:
        ...

    if not verify_password(signin_data.password, user.password):
        raise UserValidateException()

    return user