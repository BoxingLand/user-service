from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SignupRequest(_message.Message):
    __slots__ = ("account_type", "phone_number", "email", "password", "password_confirm")
    ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_CONFIRM_FIELD_NUMBER: _ClassVar[int]
    account_type: str
    phone_number: str
    email: str
    password: str
    password_confirm: str
    def __init__(self, account_type: _Optional[str] = ..., phone_number: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., password_confirm: _Optional[str] = ...) -> None: ...

class SignupResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class SigninRequest(_message.Message):
    __slots__ = ("email", "phone_number", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    phone_number: str
    password: str
    def __init__(self, email: _Optional[str] = ..., phone_number: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class SigninResponse(_message.Message):
    __slots__ = ("token_type", "access_token", "refresh_token")
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    token_type: str
    access_token: str
    refresh_token: str
    def __init__(self, token_type: _Optional[str] = ..., access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ...) -> None: ...

class ChangePasswordRequest(_message.Message):
    __slots__ = ("current_password", "new_password", "new_password_confirm", "user_id")
    CURRENT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_CONFIRM_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    current_password: str
    new_password: str
    new_password_confirm: str
    user_id: str
    def __init__(self, current_password: _Optional[str] = ..., new_password: _Optional[str] = ..., new_password_confirm: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class ChangePasswordResponse(_message.Message):
    __slots__ = ("token_type", "access_token", "refresh_token")
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    token_type: str
    access_token: str
    refresh_token: str
    def __init__(self, token_type: _Optional[str] = ..., access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ...) -> None: ...

class UpdateUserProfileRequest(_message.Message):
    __slots__ = ("first_name", "last_name", "middle_name", "birthday", "country", "region", "city", "user_id")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_NAME_FIELD_NUMBER: _ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    middle_name: str
    birthday: str
    country: str
    region: str
    city: str
    user_id: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., middle_name: _Optional[str] = ..., birthday: _Optional[str] = ..., country: _Optional[str] = ..., region: _Optional[str] = ..., city: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class UpdateUserProfileResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class AddRoleRequest(_message.Message):
    __slots__ = ("account_type", "user_id")
    ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    account_type: str
    user_id: str
    def __init__(self, account_type: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class AddRoleResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class DeleteUserResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
