import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

_SQLALCHEMY_DATABASE_URL = (
    f'{os.environ["DB_ENGINE"]}://'
    f'{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@'
    f'{os.environ["DB_HOST"]}:{os.environ["DB_PORT"]}/'
    f'{os.environ["DB_NAME"]}'
)

engine = create_engine(
    _SQLALCHEMY_DATABASE_URL,
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
