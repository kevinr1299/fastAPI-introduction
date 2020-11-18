

from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from models.user import User, UserManager
import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='api/auth/')


class AuthJWT:

    _KEY = settings.SECRET_KEY
    _ALGORITHM = settings.ALGORITHM
    _EXPIRE = settings.ACCESS_TOKEN_EXPIRE_MINUTES

    @classmethod
    def create_token(cls, user_id: int) -> str:
        expire = datetime.utcnow() + timedelta(minutes=cls._EXPIRE)
        return jwt.encode(
            {
                'sub': str(user_id),
                'exp': expire,
            },
            cls._KEY,
            algorithm=cls._ALGORITHM,
        )

    @classmethod
    def check_token(cls, token: str) -> User:
        try:
            payload = jwt.decode(token, cls._KEY, algorithms=[cls._ALGORITHM])
            return UserManager.find(payload.get('sub'))
        except JWTError:
            return None

    @classmethod
    async def get_current_user(cls, token: str = Depends(oauth2_scheme)):
        user = cls.check_token(token)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid credentials',
            )
        return user
