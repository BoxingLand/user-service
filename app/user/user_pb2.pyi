from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UserBoxerProfileRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class UserBoxerProfileResponse(_message.Message):
    __slots__ = ("first_name", "last_name", "sex", "birthday", "country", "region", "weight", "height", "athletic_distinction", "avatar")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    SEX_FIELD_NUMBER: _ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ATHLETIC_DISTINCTION_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    sex: str
    birthday: str
    country: str
    region: str
    weight: float
    height: float
    athletic_distinction: str
    avatar: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., sex: _Optional[str] = ..., birthday: _Optional[str] = ..., country: _Optional[str] = ..., region: _Optional[str] = ..., weight: _Optional[float] = ..., height: _Optional[float] = ..., athletic_distinction: _Optional[str] = ..., avatar: _Optional[str] = ...) -> None: ...

class BoxersRequest(_message.Message):
    __slots__ = ("first_name", "last_name", "club", "country", "region", "athletic_distinction", "sex", "min_weight", "max_weight", "min_height", "max_height", "min_age", "max_age", "min_birthday", "max_birthday", "page", "page_size")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUB_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    ATHLETIC_DISTINCTION_FIELD_NUMBER: _ClassVar[int]
    SEX_FIELD_NUMBER: _ClassVar[int]
    MIN_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    MAX_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    MIN_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    MAX_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    MIN_AGE_FIELD_NUMBER: _ClassVar[int]
    MAX_AGE_FIELD_NUMBER: _ClassVar[int]
    MIN_BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    MAX_BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    club: str
    country: str
    region: str
    athletic_distinction: str
    sex: str
    min_weight: float
    max_weight: float
    min_height: float
    max_height: float
    min_age: int
    max_age: int
    min_birthday: str
    max_birthday: str
    page: int
    page_size: int
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., club: _Optional[str] = ..., country: _Optional[str] = ..., region: _Optional[str] = ..., athletic_distinction: _Optional[str] = ..., sex: _Optional[str] = ..., min_weight: _Optional[float] = ..., max_weight: _Optional[float] = ..., min_height: _Optional[float] = ..., max_height: _Optional[float] = ..., min_age: _Optional[int] = ..., max_age: _Optional[int] = ..., min_birthday: _Optional[str] = ..., max_birthday: _Optional[str] = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ...) -> None: ...

class BoxersResponse(_message.Message):
    __slots__ = ("first_name", "last_name", "club", "country", "region", "weight", "birthday", "athletic_distinction", "avatar")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUB_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    ATHLETIC_DISTINCTION_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    club: str
    country: str
    region: str
    weight: float
    birthday: str
    athletic_distinction: str
    avatar: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., club: _Optional[str] = ..., country: _Optional[str] = ..., region: _Optional[str] = ..., weight: _Optional[float] = ..., birthday: _Optional[str] = ..., athletic_distinction: _Optional[str] = ..., avatar: _Optional[str] = ...) -> None: ...

class UploadFileRequest(_message.Message):
    __slots__ = ("file_content", "is_avatar", "content_type", "user_id")
    FILE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    IS_AVATAR_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    file_content: bytes
    is_avatar: bool
    content_type: str
    user_id: str
    def __init__(self, file_content: _Optional[bytes] = ..., is_avatar: bool = ..., content_type: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class UploadFileResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("first_name", "last_name", "sex", "middle_name", "birthday", "country", "region", "city", "user_id")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    SEX_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_NAME_FIELD_NUMBER: _ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    sex: str
    middle_name: str
    birthday: str
    country: str
    region: str
    city: str
    user_id: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., sex: _Optional[str] = ..., middle_name: _Optional[str] = ..., birthday: _Optional[str] = ..., country: _Optional[str] = ..., region: _Optional[str] = ..., city: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

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
