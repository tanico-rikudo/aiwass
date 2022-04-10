from typing import Optional

from pydantic import BaseModel, Field
from datetime import datetime

class PredictionBase(BaseModel):
    symbol: str = Field(None, example="BTC")
    time: int = Field(None, example="20220215114733760925")
    name: float = Field(None, example="price_signal")
    value: float = Field(None, example="1342645.0")
    
class TradeResponseBase(PredictionBase):
    time: datetime
    
class PredictionResponseBase(BaseModel):
    symbol: str = Field(None, example="BTC")
    time: str = Field(None, example="20220215114733760925")
    name: float = Field(None, example="price_signal")
    value: float = Field(None, example="1342645.0")

    
