import datetime

from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from store.models.models import User
from store import user as user_db

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=['bcrypt'])


def hash_password(password):
    return pwd_context.hash(password)


def verify_password(password, password_hash):
    return pwd_context.verify(password, password_hash)


def generate_token(user: User):
    data = {
        "exp": datetime.datetime.now() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        'sub': user.login
    }
    token = jwt.encode(data, SECRET_KEY, ALGORITHM)
    return token


def auth(session: Session, login, password):
    user = user_db.get_user_by_username(session, login)
    if user is None:
        raise ValueError("Логин или пароль неверен")
    res = verify_password(password, user.password_hash)
    if not res:
        raise ValueError("Логин или пароль неверен")
    return generate_token(user)


def register(session: Session, user: User):
    user.password_hash = hash_password(user.password_hash)
    return user_db.add_user(session, user)
