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


def change_users_name_by_id(user_id: int, new_name: str):
    with session_factory() as session:
        session: Session
        user = session.query(User).filter_by(id=user_id).first()
        user.name = new_name
        session.commit()


def change_users_name_by_login(login: str, new_name: str):
    with session_factory() as session:
        session: Session
        user = session.query(User).filter_by(login=login).first()
        user.name = new_name
        session.commit()


def change_users_surname_by_id(user_id: int, new_surname: str):
    with session_factory() as session:
        session: Session
        user = session.query(User).filter_by(id=user_id).first()
        user.surname = new_surname
        session.commit()


def change_users_surname_by_login(login: str, new_surname: str):
    with session_factory() as session:
        session: Session
        user = session.query(User).filter_by(login=login).first()
        user.surname = new_surname
        session.commit()
