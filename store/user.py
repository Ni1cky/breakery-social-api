from sqlalchemy.orm import Session
from store import session_factory
from store.models.models import User


def add_user(user: User):
    with session_factory() as session:
        session: Session
        session.add(user)
        session.commit()


def get_user_by_id(user_id: int) -> User:
    with session_factory() as session:
        session: Session
        user = session.query(User).filter_by(id=user_id).first()
        return user


def get_user_by_login(login: str) -> User:
    with session_factory() as session:
        session: Session
        user = session.query(User).filter_by(login=login).first()
        return user


def delete_user(user: User):
    with session_factory() as session:
        session: Session
        session.delete(user)
