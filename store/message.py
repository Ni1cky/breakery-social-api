from sqlalchemy import and_, or_
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


def messages_from_to(user1_id: int, user2_id: int):
    with session_factory() as session:
        session: Session
        # messages = session.query(Message).filter_by(sender_id=from_id, receiver_id=to_id).all()
        # messages = session.query(Message).filter(
        #     (Message.sender_id == from_id and Message.receiver_id == to_id) or
        #     (Message.sender_id == to_id and Message.receiver_id == from_id)
        # ).all()
        messages = session.query(Message).filter(
            or_(
                and_(Message.sender_id == user1_id, Message.receiver_id == user2_id),
                and_(Message.sender_id == user2_id, Message.receiver_id == user1_id)
            )
        ).all()
        print(messages)
        return messages
