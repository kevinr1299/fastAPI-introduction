from __future__ import annotations

from passlib.context import CryptContext


class Crypt:

    _CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def hash(cls, text: str) -> str:
        return cls._CONTEXT.hash(text)

    @classmethod
    def check(cls, text: str, hash: str) -> bool:
        return cls._CONTEXT.verify(text, hash)
