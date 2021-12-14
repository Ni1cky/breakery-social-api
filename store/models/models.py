from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    name = Column(String)
    surname = Column(String)
    photo = Column(String)
    additional_data = Column(String)


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    time_send = Column(DateTime)
    is_read = Column(Boolean)
    is_important = Column(Boolean)
    is_edited = Column(Boolean)
