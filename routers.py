from fastapi import APIRouter, Body, Depends, status

from authentication import AuthJWT
from schemas.autnetication import TokenData
from schemas.user import (
    User,
    UserCreation,
    UserSignIn,
)
from services import UserService

router = APIRouter()


@router.post('', tags=['auth'])
async def sign_in(data: UserSignIn = Body(...)):
    return UserService.sign_in(data)


@router.post(
    '/sign_up',
    tags=['auth'],
    response_model=User,
    status_code=status.HTTP_201_CREATED
)
async def sign_up(data: UserCreation = Body(...)):
    return UserService.create_user(data)


@router.post('/verify', tags=['auth'])
async def verify_token(data: TokenData = Body(...)):
    return UserService.verify_token(data.token)


@router.post('/sign_out', tags=['auth'])
async def sign_out(user: User = Depends(AuthJWT.get_current_user)):
    return user
