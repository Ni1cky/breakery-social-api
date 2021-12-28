from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import Depends
from jose import jwt

from starlette.responses import JSONResponse
import authorization
from store.models.models import User
from store.models.schemes import UserCreate, UserGet
from store.user import get_user_by_id, add_user, delete_user, get_users, update_user, session_factory
from store import user as user_store

auth_router = APIRouter()


def get_db():
    db = session_factory()
    try:
        yield db
    finally:
        db.close()

auth_scheme = OAuth2PasswordBearer(tokenUrl='token')

def current_user(token: str = Depends(auth_scheme), session: Session = Depends(get_db)):
    data = jwt.decode(token, authorization.SECRET_KEY, authorization.ALGORITHM)
    if data.get('sub') is None:
        raise JWTError("sub is not found in token")
    user = user_store.get_user_by_username(session, data['sub'])
    if user is None:
        raise JWTError("user is not found in db")
    return user

@app.post('/token')
def token(form: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db)):
    try:
        token = authorization.auth(session, form.username, form.password)
    except ValueError:
        return JSONResponse(status_code=401)
    else:
        return {"access_token": token, "token_type": "bearer"}


@app.get('/users/me', response_model=UserGet)
def get_me(current_user: User = Depends(current_user)):
    return current_user


@app.post('/auth/register')
def register(user: UserCreate, session: Session = Depends(get_db)):
    return authorization.register(session, User(**user.dict()))



