from typing import List

from sqlalchemy import Column, Integer, String

from models.db import Base, Session
from utils import Crypt


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(64))


class UserManager:

    _DB = Session()

    @classmethod
    def find(cls, user_id: int) -> User:
        return cls._DB.query(User).get(user_id)

    @classmethod
    def get(cls) -> List[User]:
        return cls._DB.query(User).all()

    @classmethod
    def get_by_email(cls, email: str) -> User:
        return cls._DB.query(User).filter_by(email=email).first()

    @classmethod
    def save(cls, data) -> User:
        password = Crypt.hash(data.password)
        user = User(email=data.email, password=password)
        cls._DB.add(user)
        cls._DB.commit()
        return user

    @classmethod
    def delete(cls, user_id: int) -> bool:
        user = cls.get_user(user_id)
        if not user:
            return False
        cls._DB.delete(user)
        cls._DB.commit()
        return True
