from fastapi import APIRouter

from store.dialog import get_dialog_by_id, add_dialog
from store.models.models import Dialog

dialog_router = APIRouter()


@dialog_router.get("/dialogs/{dialog_id}")
def get_dialog(dialog_id: int):
    dialog = get_dialog_by_id(dialog_id)
    return dialog


@dialog_router.post("/dialogs")
def create_dialog(req_dialog):
    dialog = Dialog(**req_dialog.dict)
    add_dialog(dialog)
