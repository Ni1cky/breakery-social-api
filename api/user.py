from api import app
from store.models.models import User
from store.user import get_user_by_id, get_user_by_login, add_user, delete_user, change_users_name_by_id, \
    change_users_name_by_login


@app.get("/get_user")
def get_user(user_id: int = -1, login: str = "") -> User:
    if user_id != -1:
        user = get_user_by_id(user_id)
        return user
    if login:
        user = get_user_by_login(login)
        return user
    print("Дурак?")


@app.post("/add_user/{user}")
def add_new_user(user: User):
    add_user(user)


@app.delete("/delete_user/{user}")
def delete_the_user(user: User):
    delete_user(user)


@app.post("/change_name")
def change_users_name(user_id: int = -1, login: str = "", new_name: str = ""):
    if not new_name:
        print("Дурак?")
        return

    if user_id != -1:
        change_users_name_by_id(user_id, new_name)
        return
    if login:
        change_users_name_by_login(login, new_name)
        return
    print("Дурак?")


@app.post("/change_surname")
def change_users_surname(user_id: int = -1, login: str = "", new_surname: str = ""):
    if not new_surname:
        print("Дурак?")
        return

    if user_id != -1:
        change_users_name_by_id(user_id, new_surname)
        return
    if login:
        change_users_name_by_login(login, new_surname)
        return
    print("Дурак?")
