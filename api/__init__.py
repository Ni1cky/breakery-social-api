from fastapi import FastAPI
from api.dialog import dialog_router
from api.message import message_router
from api.user import user_router
from api.auth import auth_router
from api.subscriptions import subscriptions_router
from api.photo import photo_router
from api.posts import posts_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(message_router)
app.include_router(subscriptions_router)
app.include_router(photo_router)
app.include_router(dialog_router)
app.include_router(posts_router)
