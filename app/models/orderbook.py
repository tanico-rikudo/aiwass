import os,sys
from datetime import datetime as dt
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN, FLOAT, DATETIME

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(sys.path)
from db.db import Base

import hashlib

class OrderBook(Base):
    """
    Learning model  

    ID       : Primary 
    TIME: datetime
    SYMBOL  : symbol (unique)
    PRICE:  price
    FLAG01 : option value
    FLAG02 : option value
    FLAG03 : option value
    """
    __tablename__ = 'Orderbook'
    id = Column( 'id',INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    time = Column('TIME', DATETIME,nullable=False)
    symbol = Column('SYMBOL', String(256),nullable=False)
    bids0 = Column('BIDS0', FLOAT(256), nullable=False)
    bids0_size = Column('BIDS0_SIZE', FLOAT(256), nullable=False)
    asks0 = Column('ASKS0', FLOAT(256), nullable=False)
    asks0_size = Column('ASKS0_SIZE', FLOAT(256), nullable=False)


    def __init__(self, symbol, time,  bids0, bids0_size, asks0, asks0_size, **kwargs):
        self.symbol = symbol
        self.time = time
        self.bids0 = bids0
        self.bids0_size = bids0_size
        self.asks0 = asks0
        self.asks0_size = asks0_size
    

    def __str__(self):
        return f"{self.id} :{self.symbol}  -->  ask0:{self.asks0}@{self.asks0_size} - bid0:{self.bids0}) - bid:{self.bids0_size}"