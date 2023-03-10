from fastapi import APIRouter, Depends

from api.auth import current_user
from store.posts import get_post_by_id, add_post, delete_post, update_post, get_user_posts, get_posts, get_max_post_id
from store.models.models import Post
from store.models.schemes import PostBase
from sqlalchemy.orm import Session
from store.posts import session_factory
from fastapi import Depends
from store.models.models import User
posts_router = APIRouter()


def get_db():
    db = session_factory()
    try:
        yield db
    finally:
        db.close()


@posts_router.get("/posts/{posts_id}")
def get_post(posts_id: int, session: Session = Depends(get_db), user: User = Depends(current_user)):
    posts = get_post_by_id(posts_id, session)
    return posts


@posts_router.post("/newpost")
def add_new_post(req_posts: PostBase, session: Session = Depends(get_db), user: User = Depends(current_user)):
    posts = Post(**req_posts.dict())
    add_post(posts, session)
    return posts.id


@posts_router.delete("/posts/{posts_id}")
def delete_the_post(posts_id: int, session: Session = Depends(get_db), user: User = Depends(current_user)):
    delete_post(posts_id, session)


@posts_router.put("/posts/{posts_id}/edit")
def change_posts_fields(posts_id: int, req_posts, session: Session = Depends(get_db), user: User = Depends(current_user)):
    posts = Post(**req_posts.dict())
    update_post(posts, session)


@posts_router.get("/posts/{user_id}/all")
def get_all_user_posts(user_id: int, session: Session = Depends(get_db), user: User = Depends(current_user)):
    posts = get_user_posts(user_id, session)
    return posts


@posts_router.get("/posts")
def get_all_posts(min_id: int, max_id: int, session: Session = Depends(get_db), user: User = Depends(current_user)):
    posts = get_posts(min_id, max_id, session)
    return posts


@posts_router.get("/posts_last_id")
def get_id_of_last_post(session: Session = Depends(get_db), user: User = Depends(current_user)):
    post_id = get_max_post_id(session)
    return post_id
