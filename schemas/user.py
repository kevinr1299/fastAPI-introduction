from pydantic import BaseModel, Field, ValidationError, validator

from models.user import UserManager

EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"


class UserBase(BaseModel):

    email: str = Field(..., regex=EMAIL_REGEX)


class UserSignIn(UserBase):

    password: str


class UserCreation(UserSignIn):

    confirmation: str

    @validator('email')
    def unique_email(cls, v):
        if UserManager.get_by_email(v):
            raise ValidationError('Email already taken')
        return v

    @validator('confirmation')
    def password_match(cls, v, values, **kwargs):
        if v != values['password']:
            raise ValidationError('Password and confirmation must be a match')
        return v


class User(UserBase):

    id: int

    class Config:
        orm_mode = True
