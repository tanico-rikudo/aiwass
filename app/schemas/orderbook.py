from typing import Optional

from pydantic import BaseModel, Field
from datetime import datetime

class OrderBookBase(BaseModel):
    symbol: str = Field(None, example="BTC")
    time: str = Field(None, example="20220215114733760925")
    bids0: float = Field(None, example="1342645.0")
    bids0_size: float = Field(None, example="100")
    asks0: float = Field(None, example="1342645.0")
    asks0_size: float = Field(None, example="100")

    
class OrderBookResponseBase(OrderBookBase):
    time: str
