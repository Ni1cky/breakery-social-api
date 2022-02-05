from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


likes_table = Table('association', Base.metadata,
                    Column('user_id', Integer, ForeignKey('users.id')),
                    Column('post_id', Integer, ForeignKey('posts.id')))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    name = Column(String)
    surname = Column(String)
    photo = Column(String)
    additional_data = Column(String)
    posts = relationship("Post", backref="author")
    liked_posts = relationship("Post", backref="user", cascade='all,delete,save-update', secondary=likes_table)


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
    time_created = Column(String)
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


class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    source = Column(String)
    is_profile_picture = Column(Boolean)
    post_id = Column(Integer, ForeignKey("posts.id"))
