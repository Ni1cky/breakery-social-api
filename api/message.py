from fastapi import APIRouter

from api.auth import current_user
from store.message import get_message_by_id, add_message, delete_message, update_message, messages_for_dialog
from store.models.models import Message
from store.models.schemes import MessageCreate
from fastapi import Depends
from store.models.models import User
message_router = APIRouter()


# @message_router.get("/messages/{message_id}")
# def get_message(message_id: int):
#     message = get_message_by_id(message_id)
#     return message


@message_router.post("/messages")
def add_new_message(req_message: MessageCreate, user: User = Depends(current_user)):
    message = Message(**req_message.dict())
    add_message(message)


@message_router.delete("/messages/{message_id}")
def delete_the_message(message_id: int, user: User = Depends(current_user)):
    delete_message(message_id)


@message_router.put("/messages/{message_id}/edit")
def change_messages_fields(message_id: int, req_message, user: User = Depends(current_user)):
    message = Message(**req_message.dict())
    update_message(message)


@message_router.get("/messages/{user_id}")
def get_messages_by_ids_in_dialogue(user_id: int, user1: User = Depends(current_user)):
    messages = messages_for_dialog(user1.id, user_id)
    return messages
