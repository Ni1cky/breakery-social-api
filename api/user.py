from api import app
from store.models.models import User
from store.user import get_user_by_id, add_user, delete_user, get_users, update_user


@app.get("/users")
def get_all_users():
    users = get_users()
    return users


@app.post("/users")
def add_new_user(req_user):
    user = User(**req_user.dict)
    add_user(user)


@app.delete("/users/{user_id}")
def delete_the_user(user_id: int):
    delete_user(user_id)


@app.post("/users/{user_id}/edit")
def change_users_name(user_id: int, req_user):
    user = User(**req_user.dict)
    update_user(user)


@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = get_user_by_id(user_id)
    return user
