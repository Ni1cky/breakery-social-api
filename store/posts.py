from sqlalchemy.orm import Session
from store import session_factory
from store.models.models import Post


def add_post(post: Post, session: Session):
    session.add(post)
    session.commit()


def get_max_post_id(session: Session):
    try:
        post = session.query(Post).order_by(Post.id.desc()).first()
        return post.id
    except:
        return None


def get_posts(min_id: int, max_id: int, session: Session):
    try:
        posts = session.query(Post).where(min_id < Post.id, Post.id <= max_id).all()
        return posts
    except:
        return None


def get_post_by_id(post_id: int, session: Session):
    try:
        post = session.query(Post).filter_by(id=post_id).first()
        return post
    except:
        return None


def delete_post(post_id: int, session: Session):
    try:
        post = session.query(Post).filter_by(id=post_id).first()
        session.delete(post)
        session.commit()
    except:
        return None


def update_post(post: Post, session: Session):
    try:
        session.add(post)
        session.commit()
    except:
        return None


def get_user_posts(user_id: int, session: Session):
    try:
        posts = session.query(Post).filter_by(author_id=user_id).all()
        return posts
    except:
        return None