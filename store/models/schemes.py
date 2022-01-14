import datetime
from typing import List
from pydantic import BaseModel
from pydantic.typing import Optional


class PostBase(BaseModel):
    text: str
    time_created: datetime.datetime
    author_id: int


class Post(PostBase):
    id: int


class PostCreate(PostBase):
    pass


class UserBase(BaseModel):
    login: str
    password_hash: str
    name: str
    surname: str
    photo: Optional[str]
    additional_data: Optional[str]


class User(UserBase):
    id: int
    posts: List[Post]


class UserCreate(UserBase):
    pass

class UserGet(UserBase):
    id: int

    class Config:
        orm_mode = True

class MessageBase(BaseModel):
    text: str
    time_send: datetime.datetime
    is_read: bool
    is_important: bool
    is_edited: bool
    sender_id: int
    receiver_id: int


class Message(MessageBase):
    id: int


class MessageCreate(MessageBase):
    pass
