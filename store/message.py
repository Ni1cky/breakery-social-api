from sqlalchemy.orm import Session

from store import session_factory
from store.models.models import Message


def add_message(message: Message):
    with session_factory() as session:
        session: Session
        session.add(message)
        session.commit()


def get_message_by_id(message_id: int) -> Message:
    with session_factory() as session:
        session: Session
        message = session.query(Message).filter_by(id=message_id).first()
        return message


def delete_message(message: Message):
    with session_factory() as session:
        session: Session
        session.delete(message)
        session.commit()


def change_messages_text_by_id(message_id: int, new_text: str):
    with session_factory() as session:
        session: Session
        message = session.query(Message).filter_by(id=message_id).first()
        message.text = new_text
        session.commit()
