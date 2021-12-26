from fastapi import FastAPI
from api.message import message_router
from api.user import user_router
from api.auth import auth_router

app = FastAPI()
app.include_router(user_router)
app.include_router(message_router)
app.include_router(auth_router)
