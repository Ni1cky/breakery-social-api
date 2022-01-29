from sqlalchemy.orm import Session
from store.models.models import Photo, User
from store import session_factory


def get_all_user_photos(user_id: int):
    with session_factory() as session:
        session: Session
        photos = session.query(Photo).filter_by(user_id=user_id).all()
        return photos


def update_profile_picture(user_id: int, img: str):
    with session_factory() as session:
        session: Session
        photo = session.query(Photo).filter_by(user_id=user_id, is_profile_picture=True).first()
        photo.source = img
        session.commit()


def get_profile_picture(user_id: int):
    with session_factory() as session:
        session: Session
        photo = session.query(Photo).filter_by(user_id=user_id, is_profile_picture=True).first()
        return photo.source


def set_default_profile_picture(login: str, img: str):
    with session_factory() as session:
        session: Session
        user = session.query(User).filter_by(login=login).first()
        photo = Photo(user_id=user.id, source=img, is_profile_picture=True)
        session.add(photo)
        session.commit()
