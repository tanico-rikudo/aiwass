from typing import Optional

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    user_id: str = Field(None, example="1234567")
    user_name: str = Field(None, example="shirotan")
    mail: str = Field(None, example="shirotan@test.com")


class UserCreate(UserBase):
    """ Request schema 

    Args:
        UserBase ([type]): [description]
    """
    pass


class UserCreateResponse(UserCreate):
    """ Create  response schema

    Args:
        UserCreate ([type]): [description]
    """
    id: int
    class Config:
        orm_mode = True


class User(UserBase):
    """ Get user

    Args:
        UserBase ([type]): [description]
    """
    id: int
    user_id: str = Field(None, example="Test005")
    user_name: str = Field(None, example="slstm")

    class Config:
        orm_mode = True
