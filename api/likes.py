from fastapi import APIRouter
from store.likes import add_like_to_post, remove_like, get_all_post_likes, get_all_like_posts
from api.auth import current_user
from fastapi import Depends
from store.models.models import User

likes_router = APIRouter()


@likes_router.post("/likes/{user_id}/{post_id}")
def add_like(user_id: int, post_id: int, user: User = Depends(current_user)):
    add_like_to_post(user_id, post_id)


@likes_router.delete("/likes/{user_id}/{post_id}")
def delete_like(user_id: int, post_id: int, user: User = Depends(current_user)):
    remove_like(user_id, post_id)


@likes_router.get("/likes/{post_id}")
def get_post_likes(post_id: int, user: User = Depends(current_user)):
    users = get_all_post_likes(post_id)
    return users


@likes_router.get("/likes/{user_id}/all")
def get_like_posts(user_id: int, user: User = Depends(current_user)):
    posts = get_all_like_posts(user_id)
    return posts
