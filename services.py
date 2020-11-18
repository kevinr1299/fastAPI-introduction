from __future__ import annotations

from fastapi import HTTPException, status

from authentication import AuthJWT
from models.user import User, UserManager
from schemas.user import (
    UserCreation,
    UserSignIn,
)
from utils import Crypt


class UserService:

    @staticmethod
    def create_user(data: UserCreation) -> User:
        return UserManager.save(data)

    @staticmethod
    def sign_in(data: UserSignIn) -> dict:
        user = UserManager.get_by_email(data.email)
        if not (user and Crypt.check(data.password, user.password)):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid credentials',
            )
        return {'token': AuthJWT.create_token(user.id)}

    @staticmethod
    def verify_token(token: str):
        if not AuthJWT.check_token(token):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid token'
            )
