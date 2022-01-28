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
