from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    name = Column(String)
    surname = Column(String)
    photo = Column(String)
    additional_data = Column(String)
    posts = relationship("Post", backref="user")


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    time_send = Column(DateTime)
    is_read = Column(Boolean)
    is_important = Column(Boolean)
    is_edited = Column(Boolean)
    sender_id = Column(Integer, ForeignKey("users.id"))
    dialog_id = Column(Integer, ForeignKey("dialogs.id"))


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    time_created = Column(DateTime)
    author_id = Column(Integer, ForeignKey("users.id"))


class Dialog(Base):
    __tablename__ = "dialogs"

    id = Column(Integer, primary_key=True)
    user1_id = Column(Integer, ForeignKey("users.id"))
    user2_id = Column(Integer, ForeignKey("users.id"))
    messages = relationship("Message", backref="dialog")


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    subscriber_id = Column(Integer, ForeignKey("users.id"))
    is_banned = Column(Boolean)
