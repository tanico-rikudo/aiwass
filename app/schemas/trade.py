from typing import Optional

from pydantic import BaseModel, Field
from datetime import datetime

class TradeBase(BaseModel):
    symbol: str = Field(None, example="BTC")
    time: int = Field(None, example="20220215114733760925")
    price: float = Field(None, example="1342645.0")
    size: float = Field(None, example="100")
    price: float = Field(None, example="20200101")
    
class TradeResponseBase(TradeBase):
    time: datetime
    
class OhlcvResponseBase(BaseModel):
    symbol: str = Field(None, example="BTC")
    time: str = Field(None, example="20220215114733760925")
    open: float = Field(None, example="1342645.0")
    high: float = Field(None, example="1342645.0")
    low: float = Field(None, example="1342645.0")
    close: float = Field(None, example="1342645.0")
    size: float = Field(None, example="1342645.0")

    
