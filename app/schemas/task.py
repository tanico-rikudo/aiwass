from typing import Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    model_id: str = Field(None, example="Test0055")
    model_name: str = Field(None, example="slstm")
    status: str = Field(None, example="registered")


class TaskCreate(TaskBase):
    """ Request schema 

    Args:
        TaskBase ([type]): [description]
    """
    pass


class TaskCreateResponse(TaskCreate):
    """ Create  response schema

    Args:
        TaskCreate ([type]): [description]
    """
    id: int
    class Config:
        orm_mode = True


class Task(TaskBase):
    """ Get task

    Args:
        TaskBase ([type]): [description]
    """
    id: int
    model_id: str = Field(None, example="Test005")
    model_name: str = Field(None, example="slstm")
    status: str = Field(None, example="registered")

    class Config:
        orm_mode = True
