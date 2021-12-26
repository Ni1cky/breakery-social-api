import datetime

from passlib.context import CryptContext

from jose import jwt


from store.models.models import User
from store import user as user_db

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=['bcrypt'])


def verify_pass(password, hash_password):
    return pwd_context.verify(password, hash_password)


def create_token(user: User):
    data = {
        'exp': datetime.datetime.now() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        'sub': str(user.id)
    }

    token = jwt.encode(data, SECRET_KEY, ALGORITHM)
    return token


def auth(session, login, password):
    user = user_db.get_user_by_name(session, login)
    if user is None:
        raise ValueError('такого пользователя не сущетсвует')
    res = verify_pass(password, user.password)
    if not res:
        raise ValueError('Логин или пароль неверны')
    else:
        return create_token(user)


def register(session, user: User):
    user.password = pwd_context.hash(user.password)
    user_db.add_new_user(session, user)
