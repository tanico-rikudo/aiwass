from datetime import datetime as dt

from db import Base

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN

import hashlib

SQLITE3_NAME = "./db.sqlite3"


class Task(Base):
    """
    Learning model  

    ID       : Primary 
    MODEL_ID  : model id (unique)
    MODEL_NAME: model name
    TRAIN_START_DATE : train date(start)
    TRAIN_START_DATE : train date(end)
    VALID_START_DATE : valid date(start)
    VALID_START_DATE : valid date(end)
    TEST_START_DATE : test date(start)
    TEST_START_DATE : test date(end)
    STATUS:  status
    """
    __tablename__ = 'Task'
    id = Column( 'id',INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    model_id = Column('MODEL_ID', String(256),nullable=False,unique=True)
    model_name = Column('MODEL_NAME', String(256), nullable=False)
    train_start_date = Column('TRAIN_START_DATE', String(256),nullable=False)
    train_end_date = Column('TRAIN_END_DATE', String(256), nullable=False)
    valid_start_date = Column('VALID_START_DATE', String(256))
    valid_end_date = Column('VALID_END_DATE', String(256))
    test_start_date = Column('TEST_START_DATE', String(256))
    test_end_date = Column('TEST_END_DATE', String(256))
    status = Column("STATUS",String(256))

    def __init__(self, model_name, **kwargs):
        self.model_id = hex(int(dt.now().strftime("%Y%m%d%H%M%s")))
        self.model_name = model_name

        arg_keys = kwargs.keys()
        print(arg_keys)
        if ("TRAIN_START_DATE" in arg_keys)and("TRAIN_END_DATE" in arg_keys):
            self.train_start_date =  kwargs["TRAIN_START_DATE"]
            self.train_end_date =   kwargs["TRAIN_END_DATE"]
    
        if ("VALID_START_DATE" in arg_keys)and("VALID_END_DATE" in arg_keys):
            self.valid_start_date =   kwargs["VALID_START_DATE"]
            self.valid_end_date =  kwargs["VALID_END_DATE"]
    
        if ("TEST_START_DATE" in arg_keys)and("TEST_END_DATE" in arg_keys):
            self.test_start_date =  kwargs["TEST_START_DATE"]
            self.test_end_date = kwargs["TEST_END_DATE"]

    def __str__(self):
        return f"{self.model_id} :{self.model_name}"


class User(Base):
    """
    User table

    id       : Primary
    username : Username
    password : pass word
    mail     : mail address
    """
    __tablename__ = 'User'
    id = Column(
        'id',
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )
    username = Column('username', String(256))
    password = Column('password', String(256))
    mail = Column('mail', String(256))  
 
    def __init__(self, username, password, mail):
        self.username = username
        self.password = hashlib.md5(password.encode()).hexdigest()
        self.mail = mail
 
    def __str__(self):
        return str(self.id) + ':' + self.username