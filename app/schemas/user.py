from typing import Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    username: str = Field(None, example="tanico")
    passward: str = Field(None, example="password")
    mailaddress: str = Field(None, example="test@test.com")
