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
    is_read: bool = False
    is_important: bool = False
    is_edited: bool = False
    sender_id: int
    dialog_id: int


class Message(MessageBase):
    id: int
    send_from_me: int = -1


class MessageCreate(MessageBase):
    pass


class DialogBase(BaseModel):
    user1_id: int
    user2_id: int


class Dialog(DialogBase):
    id: int


class DialogCreate(DialogBase):
    pass
