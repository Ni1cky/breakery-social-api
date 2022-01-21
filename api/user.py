from fastapi import APIRouter
from store.models.models import User
from store.models.schemes import UserBase
from store.user import get_user_by_id, add_user, delete_user, get_users, update_user


user_router = APIRouter()


@user_router.get("/users")
def get_all_users():
    users = get_users()
    return users


@user_router.post("/users")
def add_new_user(req_user):
    user = User(**req_user.dict())
    add_user(user)


@user_router.delete("/users/{user_id}")
def delete_the_user(user_id: int):
    delete_user(user_id)


@user_router.put("/users/{user_id}/edit")
def change_users_fields(user_id: int, req_user: UserBase):
    user = User(**req_user.dict())
    update_user(user_id, user)


@user_router.get("/users/{user_id}")
def get_user(user_id: int):
    user = get_user_by_id(user_id)
    return user
