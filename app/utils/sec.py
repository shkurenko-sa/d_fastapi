from passlib.context import CryptContext
from typing import Any


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PasswordHasher:
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> Any:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)