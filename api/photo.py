from fastapi import APIRouter
from store.models.models import Photo
from store.photo import get_all_user_photos, update_profile_picture, get_profile_picture, set_default_profile_picture
from store.models.schemes import PhotoBase

photo_router = APIRouter()


@photo_router.get("/photos/{user_id}")
def get_user_photos(user_id: int):
    photos = get_all_user_photos(user_id)
    return photos


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
