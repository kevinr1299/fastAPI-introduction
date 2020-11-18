from __future__ import annotations

from typing import List

import asyncio
from fastapi import FastAPI, Depends

from authentication import AuthJWT
from models.user import User, UserManager
from routers import router
from schemas.user import User as UserSchema


app = FastAPI()


app.include_router(router, prefix='/api/auth')


@app.get('/api/users/', response_model=List[UserSchema])
async def get_users(user: User = Depends(AuthJWT.get_current_user)):
    await asyncio.sleep(10)
    return UserManager.get()
