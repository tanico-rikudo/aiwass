from typing import Optional

from pydantic import BaseModel, Field
from datetime import datetime

class TradeBase(BaseModel):
    symbol: str = Field(None, example="BTC")
    event_datetime: int = Field(None, example="20220215114733760925")
    price: float = Field(None, example="1342645.0")
    size: float = Field(None, example="100")
    ask: float = Field(None, example="1342644.5")
    bid: float = Field(None, example="1342646.5")
    price: float = Field(None, example="20200101")
    
class TradeResponseBase(TradeBase):
    event_datetime: datetime
    
class TradeCreate(TradeBase):
    """ Request schema 

    Args:
        TradeBase ([type]): [description]
    """
    pass


class TradeCreateResponse(TradeCreate):
    """ Create  response schema

    Args:
        UserCreate ([type]): [description]
    """
    id: int
    event_datetime: datetime

    class Config:
        orm_mode = True