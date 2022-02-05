from fastapi import APIRouter, Depends

from api.auth import current_user
from store.dialog import get_dialog_by_id, add_dialog, get_dialog_by_users_ids, get_users_dialogs
from store.models.models import Dialog, User
from store.models.schemes import DialogCreate

dialog_router = APIRouter()


@dialog_router.get("/dialogs/all/{user_id}")
def get_all_dialogs_for_user(user_id: int, user: User = Depends(current_user)):

    dialogs = get_users_dialogs(user_id)
    return dialogs


@dialog_router.get("/dialogs/{dialog_id}")
def get_dialog(dialog_id: int, user: User = Depends(current_user)):
    dialog = get_dialog_by_id(dialog_id)
    return dialog


@dialog_router.post("/dialogs")
def create_dialog(req_dialog: DialogCreate, user: User = Depends(current_user)):
    dialog = Dialog(**(req_dialog.dict()))
    add_dialog(dialog)


@dialog_router.get("/dialogs/{user1_id}/{user2_id}")
def get_dialog_between_two_users(user1_id: int, user2_id: int, user: User = Depends(current_user)):
    dialog = get_dialog_by_users_ids(user1_id, user2_id)
    return dialog
