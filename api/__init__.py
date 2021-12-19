from fastapi import FastAPI
from api.message import message_router
from api.user import user_router

app = FastAPI()
app.include_router(user_router)
app.include_router(message_router)
