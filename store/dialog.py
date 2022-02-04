from sqlalchemy import and_, or_
from sqlalchemy.orm import Session
from store import session_factory
from store.models.models import Dialog


def get_dialog_by_id(dialog_id: int):
    with session_factory() as session:
        session: Session
        dialog = session.query(Dialog).filter_by(id=dialog_id).first()
        return dialog


def add_dialog(dialog: Dialog):
    with session_factory() as session:
        session: Session
        session.add(dialog)
        session.commit()


def get_dialog_by_users_ids(user1_id: int, user2_id: int):
    with session_factory() as session:
        session: Session
        dialog = session.query(Dialog).filter(
            or_(and_(Dialog.user1_id == user1_id, Dialog.user2_id == user2_id),
                and_(Dialog.user1_id == user2_id, Dialog.user2_id == user1_id))
        ).first()
        return dialog


def get_users_dialogs(user_id: int):
    with session_factory() as session:
        session: Session
        dialogs = session.query(Dialog).filter(
            or_(Dialog.user1_id == user_id, Dialog.user2_id == user_id)
        ).all()
        return dialogs
