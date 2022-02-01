from sqlalchemy.orm import Session
from store import session_factory
from store.models.models import Post


def add_post(post: Post, session: Session):
    session.add(post)
    session.commit()


def get_max_post_id(session: Session):
    post = session.query(Post).order_by(Post.id.desc()).first()
    return post.id


def get_posts(min_id: int, max_id: int, session: Session):
    # posts = session.query(Post).all()
    posts = session.query(Post).where(min_id < Post.id, Post.id <= max_id).all()
    return posts


def get_post_by_id(post_id: int, session: Session) -> Post:
    post = session.query(Post).filter_by(id=post_id).first()
    return post


def delete_post(post_id: int, session: Session):
    post = session.query(Post).filter_by(id=post_id).first()
    session.delete(post)
    session.commit()


def update_post(post: Post, session: Session):
    session.add(post)
    session.commit()


def get_user_posts(user_id: int, session: Session):
    posts = session.query(Post).filter_by(author_id=user_id).all()
    return posts
