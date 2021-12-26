from fastapi import APIRouter
from store.posts import get_posts_by_id, add_posts, delete_posts, update_posts, posts_from_to
from store.models.models import Posts


posts_router = APIRouter()


@posts_router.get("/posts/{posts_id}")
def get_posts(posts_id: int):
    posts = get_posts_by_id(posts_id)
    return posts


@posts_router.post("/posts")
def add_new_posts(req_posts):
    posts = Posts(**req_posts.dict())
    add_posts(posts)


@posts_router.delete("/posts/{posts_id}")
def delete_the_posts(posts_id: int):
    delete_posts(posts_id)


@posts_router.put("/posts/{posts_id}/edit")
def change_posts_fields(posts_id: int, req_posts):
    posts = Posts(**req_posts.dict())
    update_posts(posts)


@posts_router.get("/posts/{user1_id}/{user2_id}")
def get_posts_by_ids_in_dialogue(user1_id: int, user2_id: int):
    posts = posts_from_to(user1_id, user2_id)
    return posts
