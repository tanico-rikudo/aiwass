from typing import Optional

from pydantic import BaseModel, Field, SecretStr


class UserBase(BaseModel):
    username: str = Field(None, example="shirotan")
    password: SecretStr
    mail: str = Field(None, example="shirotan@test.com")

class UserCreate(UserBase):
    """ Request schema 

    Args:
        UserBase ([type]): [description]
    """
    password: str = Field(None, example="shirotanPW")
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
    username: str = Field(None, example="shirotan")
    password: SecretStr
    mail: str = Field(None, example="shirotan@test.com")

    class Config:
        orm_mode = True
