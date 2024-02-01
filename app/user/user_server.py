from uuid import UUID

import grpc


from app.client.auth import auth_pb2_grpc, auth_pb2
from app.core.config import settings
from app.crud.photo import add_photo_to_user, update_avatar
from app.crud.user import create_user, set_verify_token, user_email_exists, user_phone_number_exists, delete_user, \
    update_user_by_id, get_user_by_id, update_user_password, is_user_role_exist, add_role_to_user, boxer_profile_by_id, \
    boxers_filtered

from app.minio_client.minio_client import minio_client
from app.user import user_pb2, user_pb2_grpc
from app.utils.authenticate import authenticate
from app.utils.password import encrypt_password, verify_password
from app.utils.verification.generate_verify_token import generate_verification_token


class User(user_pb2_grpc.UserServicer):
    async def Signup(
            self,
            request: user_pb2.SignupRequest,
            context: grpc.aio.ServicerContext,
    ) -> user_pb2.SignupResponse:
        if request.password != request.password_confirm:
            await context.abort(grpc.StatusCode.INVALID_ARGUMENT, details="PasswordNotMatch")

        # password_check = await password_validation(request.password)
        # if len(password_check):
        #     raise UserPasswordIsEasyException(details=password_check)

        email_exists = await user_email_exists(email=request.email)
        if email_exists == request.email and request.email is not None:
            await context.abort(grpc.StatusCode.ALREADY_EXISTS, details="Email")

        phone_number_exists = await user_phone_number_exists(phone_number=request.phone_number)
        if phone_number_exists == request.phone_number and request.phone_number is not None:
            await context.abort(grpc.StatusCode.ALREADY_EXISTS, details="Phone")

        request.password = encrypt_password(password=request.password)
        await create_user(signup_data=request, context=context)

        verification_token = generate_verification_token()

        await set_verify_token(
            email=request.email,
            verify_token=verification_token,
            context=context
        )

        # TODO email подтверждение переписать
        return user_pb2.SignupResponse(message="Success")

    async def Signin(
            self,
            request: user_pb2.SigninRequest,
            context: grpc.aio.ServicerContext,
    ) -> user_pb2.SigninResponse:
        user = await authenticate(signin_data=request, context=context)


        async with grpc.aio.insecure_channel("localhost:50052") as channel:
            stub = auth_pb2_grpc.AuthStub(channel)
            response = await stub.CreateTokens(auth_pb2.CreateTokensRequest(
                user_id=str(user.id)
            ))

        return user_pb2.SigninResponse(
            token_type=response.token_type,
            access_token=response.access_token,
            refresh_token=response.refresh_token

        )


    async def ChangePassword(
            self,
            request: user_pb2.ChangePasswordRequest,
            context: grpc.aio.ServicerContext,
    ) -> user_pb2.ChangePasswordResponse:
        if request.new_password != request.new_password_confirm:
            await context.abort(grpc.StatusCode.INVALID_ARGUMENT, details="PasswordNotMatch")

        user = await get_user_by_id(
            user_id=UUID(request.user_id)
        )
        if user is None:
            await context.abort(grpc.StatusCode.NOT_FOUND)

        if not verify_password(request.current_password, user.password):
            await context.abort(grpc.StatusCode.INVALID_ARGUMENT, details="WrongPassword")

        await update_user_password(
            user_id=user.id,
            new_password=encrypt_password(password=request.new_password)
        )

        async with grpc.aio.insecure_channel("localhost:50052") as channel:
            stub = auth_pb2_grpc.AuthStub(channel)
            response = await stub.CreateTokens(auth_pb2.CreateTokensRequest(
                user_id=str(user.id)
            ))

        return user_pb2.ChangePasswordResponse(
            token_type=response.token_type,
            access_token=response.access_token,
            refresh_token=response.refresh_token
        )


    async def UserBoxerProfile(
            self,
            request: user_pb2.UserBoxerProfileRequest,
            context: grpc.aio.ServicerContext,
    ) -> user_pb2.UserBoxerProfileResponse:
        data = await boxer_profile_by_id(user_id=UUID(request.user_id))
        if data is None:
            await context.abort(grpc.StatusCode.NOT_FOUND)
        avatar_url = minio_client.presigned_get_object(
            bucket_name=settings.MINIO_BUCKET,
            object_name=data.photo_name
        )
        return user_pb2.UserBoxerProfileResponse(**data.to_dict(), avatar=avatar_url)


    async def UploadFile(
            self,
            request: user_pb2.UploadFileRequest,
            context: grpc.aio.ServicerContext,
    ) -> user_pb2.UploadFileResponse:

        data_file = minio_client.put_object(
            file_data=request.file_content,
            content_type=request.content_type,
        )
        if request.is_avatar is True:
            await update_avatar(user_id=UUID(request.user_id))

        await add_photo_to_user(photo_data=request, photo_name=data_file.file_name)
        return user_pb2.UploadFileResponse(message="Photo added")


    async def AddRole(
            self,
            request: user_pb2.AddRoleRequest,
            context: grpc.aio.ServicerContext,
    ) -> user_pb2.AddRoleResponse:
        if await is_user_role_exist(
                user_id=UUID(request.user_id),
                role=request.account_type
        ) is not None:
            await context.abort(grpc.StatusCode.ALREADY_EXISTS)

        await add_role_to_user(role_data=request)

        return user_pb2.AddRoleResponse(message="Role added successfully")


    async def UpdateUserProfile(
            self,
            request: user_pb2.UpdateUserProfileRequest,
            context: grpc.aio.ServicerContext,
    ) -> user_pb2.UpdateUserProfileResponse:
        await update_user_by_id(update_data=request)
        return user_pb2.UpdateUserProfileResponse(message="User updated")


    async def DeleteUser(
            self,
            request: user_pb2.DeleteUserRequest,
            context: grpc.aio.ServicerContext,
    ) -> user_pb2.DeleteUserResponse:
        await delete_user(
            user_id=UUID(request.user_id),
        )
        return user_pb2.DeleteUserResponse(message="User deleted")

    async def Boxers(
            self,
            request: user_pb2.BoxersRequest,
            context: grpc.aio.ServicerContext,
    ) -> user_pb2.BoxersResponse:
        data = await boxers_filtered(filtered_data=request)

        for obj in data:
            avatar_url = minio_client.presigned_get_object(
                bucket_name=settings.MINIO_BUCKET,
                object_name=obj.photo_name
            )
            yield user_pb2.BoxersResponse(**obj.to_dict(), avatar=avatar_url)
