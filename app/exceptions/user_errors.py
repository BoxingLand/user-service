from typing import Any


class UserEmailExistException(Exception):
    def __init__(
            self,
            email: str | None = None,
            headers: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(f"The email {email} already exists.")
        self.status_code = 409
        self.headers = headers


class UserPhoneNumberExistException(Exception):
    def __init__(
            self,
            phone_number: str | None = None,
            headers: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(f"The phone number {phone_number} already exists.")
        self.status_code = 409
        self.headers = headers


class UserPasswordNotMatchException(Exception):
    def __init__(
            self,
            headers: dict[str, Any] | None = None,
    ) -> None:
        super().__init__("Passwords do not match.")
        self.status_code = 400
        self.headers = headers


class UserPasswordIsEasyException(Exception):
    def __init__(
            self,
            details: list[str] | None = None,
            headers: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(details)
        self.status_code = 400
        self.headers = headers


class UserCreateException(Exception):
    def __init__(
            self,
            headers: dict[str, Any] | None = None,
    ) -> None:
        super().__init__("User is not create.")
        self.status_code = 500
        self.headers = headers


class UserEmailNotFoundException(Exception):
    def __init__(
            self,
            email: str | None = None,
            headers: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(f"The email {email} not found.")
        self.status_code = 404,
        self.headers = headers,


class UserNotFoundException(Exception):
    def __init__(
            self,
            headers: dict[str, Any] | None = None,
    ) -> None:
        super().__init__("The user not found.")
        self.status_code = 404
        self.headers = headers


class UserPhoneNumberNotFoundException(Exception):
    def __init__(
            self,
            phone_number: str | None = None,
            headers: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(f"The phone number {phone_number} not found.")
        self.status_code = 404,
        self.headers = headers,


class UserValidateException(Exception):
    def __init__(
            self,
            headers: dict[str, Any] | None = None,
    ) -> None:
        super().__init__("Incorrect login details.")
        self.status_code = 404
        self.headers = headers


class UserRoleExist(Exception):
    def __init__(
            self,
            role: str | None = None,
            headers: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(f"The user have role {role}.")
        self.status_code = 409
        self.headers = headers
