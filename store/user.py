from sqlalchemy.orm import Session
from store import session_factory
from store.models.models import User
from sqlalchemy.exc import NoResultFound



def add_user(session, user: User):
    session.add(user)
    session.commit()


def get_user_by_id(user_id: int) -> User:
    with session_factory() as session:
        session: Session
        user = session.query(User).filter_by(id=user_id).first()
        return user

def get_user_by_username(session, username: str) -> User:
    try:
        user = session.query(User).filter_by(login=username).first()
        return user
    except NoResultFound:
        return None


def delete_user(user_id):
    with session_factory() as session:
        session: Session
        user = session.query(User).filter_by(id=user_id).first()
        session.delete(user)
        session.commit()

def get_users():
    with session_factory() as session:
        session: Session
        users = session.query(User).all()
        return users


def update_user(user_id: int, upd_user: User):
    with session_factory() as session:
        session: Session
        user = session.query(User).filter_by(id=user_id).first()
        user.name = upd_user.name
        user.surname = upd_user.surname
        user.photo = upd_user.photo
        session.commit()
