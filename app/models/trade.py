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
    TIME: datetime
    SYMBOL  : symbol (unique)
    PRICE:  price
    """
    __tablename__ = 'Trade'
    id = Column( 'id',INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    time = Column('TIME', DATETIME,nullable=False)
    symbol = Column('SYMBOL', String(256),nullable=False)
    price = Column('PRICE', FLOAT(256), nullable=False)
    size = Column('SIZE', FLOAT(256), nullable=False)
    

    def __init__(self, symbol, time,  price, size, ask, bid, **kwargs):
        self.symbol = symbol
        self.time = time
        self.price = price
        self.size = size
    
    def __str__(self):
        return f"{self.id} :{self.symbol}  --> {self.size}@{self.price}."