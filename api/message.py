from api import app
from store.message import get_message_by_id, add_message, delete_message
from store.models.models import Message


@app.get("/get_message")
def get_message(message_id: int = -1):
    if message_id != -1:
        message = get_message_by_id(message_id)
        return message
    print("Дурак?")


@app.post("/add_message/{message}")
def add_new_message(message: Message):
    add_message(message)


@app.delete("/delete_message/{message}")
def delete_the_message(message: Message):
    delete_message(message)
