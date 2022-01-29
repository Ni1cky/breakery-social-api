from fastapi import APIRouter
from store.photo import update_profile_picture, get_profile_picture, set_default_profile_picture, \
    add_photo_to_user_post, update_photo_from_user_post, get_photo_from_user_post, get_user_posts_photo, \
    delete_photo_from_user_post
from store.models.schemes import PhotoBase

photo_router = APIRouter()


@photo_router.get("/photos/{user_id}/profile")
def get_user_profile_picture(user_id: int):
    photo = get_profile_picture(user_id)
    return photo


@photo_router.put("/photos/{user_id}/profile")
def set_user_profile_picture(user_id: int, img: PhotoBase):
    update_profile_picture(user_id, img.source)


@photo_router.post("/photos/default")
def set_to_user_default_picture(login: str, img: PhotoBase):
    set_default_profile_picture(login, img.source)


@photo_router.post("/photos/{user_id}/{post_id}")
def add_photo_to_post(user_id: int, post_id: int, img: PhotoBase):
    add_photo_to_user_post(user_id, post_id, img.source)


@photo_router.put("/photos/{user_id}/{post_id}")
def update_photo_from_post(user_id: int, post_id: int, img: PhotoBase):
    update_photo_from_user_post(user_id, post_id, img.source)


@photo_router.get("/photos/{user_id}/{post_id}")
def get_photo_from_post(user_id: int, post_id: int):
    photo = get_photo_from_user_post(user_id, post_id)
    return photo


@photo_router.delete("/photos/{user_id}/{post_id}")
def delete_photo_from_post(user_id: int, post_id: int):
    delete_photo_from_user_post(user_id, post_id)


@photo_router.get("/photos/{user_id}")
def get_all_user_posts_photo(user_id: int):
    photos = get_user_posts_photo(user_id)
    return photos
