from fastapi import APIRouter
from store.subscriptions import get_subscribers_by_id, get_subscriptions_by_id

subscriptions_router = APIRouter()


@subscriptions_router.get("/subscriptions/{user_id}/subscribers")
def get_user_subscribers(user_id: int):
    subscribers = get_subscribers_by_id(user_id)
    return subscribers


@subscriptions_router.get("/subscriptions/{user_id}/subscriptions")
def get_user_subscriptions(user_id: int):
    subscriptions = get_subscriptions_by_id(user_id)
    return subscriptions
