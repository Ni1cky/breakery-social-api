from sqlalchemy import and_, or_
from sqlalchemy.orm import Session
from store import session_factory
from store.models.models import Message, Dialog


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


def delete_message(message_id: int):
    with session_factory() as session:
        session: Session
        message = session.query(Message).filter_by(id=message_id).first()
        session.delete(message)
        session.commit()


def update_message(message: Message):
    with session_factory() as session:
        session: Session
        session.add(message)
        session.commit()


def messages_for_dialog(user1_id: int, user2_id: int):
    with session_factory() as session:
        session: Session
        dialog = session.query(Dialog).filter(
            or_(and_(Dialog.user1_id == user1_id, Dialog.user2_id == user2_id),
                and_(Dialog.user1_id == user2_id, Dialog.user2_id == user1_id))
        ).first()
        dialog_id = dialog.id
        messages = session.query(Message).filter_by(dialog_id=dialog_id).all()
        return messages
