import re

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def encrypt_password(password: str):
    return pwd_context.hash(password)


def verify_password(password: str, encrypted_password: str):
    return pwd_context.verify(password, encrypted_password)


async def password_validation(
        password: str
) -> list:
    details: list = []

    if len(password) < 8:
        details.append("Lenght(8)")
    if not re.search(r'[A-Z]', password):
        details.append("Uppercase(1)")
    if not re.search(r'[^a-zA-Z]', password):
        details.append("NonLetter(1)")

    return details