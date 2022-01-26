from sqlalchemy.orm import Session
from store import session_factory
from store.models.models import Subscription


def get_subscribers_by_id(user_id: int):
    with session_factory() as session:
        session: Session
        subscribers = session.query(Subscription).filter_by(user_id=user_id).all()
        return subscribers


def get_subscriptions_by_id(user_id: int):
    with session_factory() as session:
        session: Session
        subscriptions = session.query(Subscription).filter_by(subscriber_id=user_id).all()
        return subscriptions
