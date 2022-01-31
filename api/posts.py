from fastapi import APIRouter, Depends
from store.posts import get_post_by_id, add_post, delete_post, update_post
from store.models.models import Post
from store.models.schemes import PostBase
from sqlalchemy.orm import Session
from store.posts import session_factory

posts_router = APIRouter()


def get_db():
    db = session_factory()
    try:
        yield db
    finally:
        db.close()


@posts_router.get("/posts/{posts_id}")
def get_post(posts_id: int, session: Session = Depends(get_db)):
    posts = get_post_by_id(posts_id, session)
    return posts


@posts_router.post("/newpost")
def add_new_post(req_posts: PostBase, session: Session = Depends(get_db)):
    posts = Post(**req_posts.dict())
    add_post(posts, session)
    return posts.id


@posts_router.delete("/posts/{posts_id}")
def delete_the_post(posts_id: int, session: Session = Depends(get_db)):
    delete_post(posts_id, session)


@posts_router.put("/posts/{posts_id}/edit")
def change_posts_fields(posts_id: int, req_posts, session: Session = Depends(get_db)):
    posts = Post(**req_posts.dict())
    update_post(posts, session)
