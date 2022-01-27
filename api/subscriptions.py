from fastapi import APIRouter
from store.subscriptions import get_subscribers_by_id, get_subscriptions_by_id, add_subscription, delete_subscription
from store.models.models import Subscription

subscriptions_router = APIRouter()


@subscriptions_router.get("/subscriptions/{user_id}/subscribers")
def get_user_subscribers(user_id: int):
    subscribers = get_subscribers_by_id(user_id)
    return subscribers


@subscriptions_router.get("/subscriptions/{user_id}/subscriptions")
def get_user_subscriptions(user_id: int):
    subscriptions = get_subscriptions_by_id(user_id)
    return subscriptions


@subscriptions_router.post("/subscriptions")
def add_new_subscription(subscriber_id: int, subscription_id: int):
    subscription = Subscription(user_id=subscription_id, subscriber_id=subscriber_id, is_banned=False)
    add_subscription(subscription)


@subscriptions_router.delete("/subscriptions")
def delete_a_subscription(subscriber_id: int, subscription_id: int):
    delete_subscription(subscriber_id, subscription_id)
