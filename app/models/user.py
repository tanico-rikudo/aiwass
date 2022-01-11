from datetime import datetime as dt

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN

from db.db import Base

import hashlib

class User(Base):
    """
    User table

    id       : Primary
    USERNAME : Username
    PASSWORD : pass word
    MAILADDRESS     : mail address
    """
    __tablename__ = 'User'
    id = Column(
        'id',
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )
    username = Column('USERNAME', String(256))
    password = Column('PASSWORD', String(256))
    mail = Column('MAILADDRESS', String(256))  
 
    def __init__(self, username, password, mail):
        self.username = username
        self.password = hashlib.md5(password.encode()).hexdigest()
        self.mail = mail
 
    def __str__(self):
        return str(self.id) + ':' + self.username