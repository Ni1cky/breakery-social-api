from store import session_factory
from store.models.models import User, Post, likes_table
from sqlalchemy.orm import Session


def add_like_to_post(user_id: int, post_id: int):
    with session_factory() as session:
        session: Session
        post = session.query(Post).filter_by(id=post_id).first()
        user = session.query(User).filter_by(id=user_id).first()
        post.user.append(user)
        session.commit()


def remove_like(user_id: int, post_id: int):
    with session_factory() as session:
        session: Session
        post = session.query(Post).filter_by(id=post_id).first()
        user = session.query(User).filter_by(id=user_id).first()
        post.user.remove(user)
        session.commit()


def get_all_post_likes(post_id: int):
    with session_factory() as session:
        session: Session
        post = session.query(Post).filter_by(id=post_id).first()
        return post.user


def get_all_like_posts(user_id: int):
    with session_factory() as session:
        session: Session
        user = session.query(User).filter_by(id=user_id).first()
        return user.liked_posts
