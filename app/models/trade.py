import os,sys
from datetime import datetime as dt
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN, FLOAT, DATETIME

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(sys.path)
from db.db import Base

import hashlib

class Trade(Base):
    """
    Learning model  

    ID       : Primary 
    EVENT_DATETIME: datetime
    SYMBOL  : symbol (unique)
    PRICE:  price
    FLAG01 : option value
    FLAG02 : option value
    FLAG03 : option value
    """
    __tablename__ = 'Trade'
    id = Column( 'id',INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    event_datetime = Column('EVENT_DATETIME', DATETIME,nullable=False)
    symbol = Column('SYMBOL', String(256),nullable=False)
    price = Column('PRICE', FLOAT(256), nullable=False)
    size = Column('SIZE', FLOAT(256), nullable=False)
    ask = Column('ASK', FLOAT(256), nullable=False)
    bid = Column('BIS', FLOAT(256), nullable=False)
    
    flag01 = Column('FLAG01', String(256),nullable=True)
    flag02 = Column('FLAG02', String(256),nullable=True)
    flag03 = Column('FLAG03', String(256),nullable=True)
    

    def __init__(self, symbol, event_datetime,  price, size, ask, bid, **kwargs):
        self.symbol = symbol
        self.event_datetime = event_datetime
        self.price = price
        self.size = size
        self.ask = ask
        self.bid = bid
    

    def __str__(self):
        return f"{self.id} :{self.symbol}  --> {self.size}@{self.price}. ( ask:{self.ask}) - bid:{self.bid}"