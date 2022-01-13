import  os,sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.requests import Request

"""
DB connector 
"""
 
Base = declarative_base()
# RDB_PATH = 'sqlite:///db.sqlite3'
RDB_PATH = 'sqlite:////Users/macico/Dropbox/btc/aiwass/storage/db.sqlite3'
ECHO_LOG = True
 
engine = create_engine(
   RDB_PATH, echo=ECHO_LOG,
   connect_args={"check_same_thread": False}

)
 
# Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db(request: Request):
   return request.state.db
