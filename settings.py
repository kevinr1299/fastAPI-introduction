import os

SECRET_KEY = os.environ['SECRET_KEY']
ALGORITHM = os.getenv('ALGORITHM', 'HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('EXPIRE_TIME', 10))
