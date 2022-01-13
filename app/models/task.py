import os,sys
from datetime import datetime as dt
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(sys.path)
from db.db import Base

import hashlib

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
        if ("train_start_date" in arg_keys)and("train_end_date" in arg_keys):
            self.train_start_date =  kwargs["train_start_date"]
            self.train_end_date =   kwargs["train_end_date"]
    
        if ("valid_start_date" in arg_keys)and("valid_end_date" in arg_keys):
            self.valid_start_date =   kwargs["valid_start_date"]
            self.valid_end_date =  kwargs["valid_end_date"]
    
        if ("test_start_date" in arg_keys)and("test_end_date" in arg_keys):
            self.test_start_date =  kwargs["test_start_date"]
            self.test_end_date = kwargs["test_end_date"]
    def __str__(self):
        return f"{self.model_id} :{self.model_name},{self.train_start_date} "