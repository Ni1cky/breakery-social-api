from fastapi import APIRouter
from store.message import get_message_by_id, add_message, delete_message, update_message, messages_from_to
from store.models.models import Message


message_router = APIRouter()


@message_router.get("/messages/{message_id}")
def get_message(message_id: int):
    message = get_message_by_id(message_id)
    return message


@message_router.post("/messages")
def add_new_message(req_message):
    message = Message(**req_message.dict())
    add_message(message)


@message_router.delete("/messages/{message_id}")
def delete_the_message(message_id: int):
    delete_message(message_id)


@message_router.put("/messages/{message_id}/edit")
def change_messages_fields(message_id: int, req_message):
    message = Message(**req_message.dict())
    update_message(message)


@message_router.get("/messages/{user1_id}/{user2_id}")
def get_messages_by_ids_in_dialogue(user1_id: int, user2_id: int):
    messages = messages_from_to(user1_id, user2_id)
    return messages
