import db.db as db
from  app.models import * 
from  app.models.user import User
from  app.models.task import Task
from  app.models.trade import Trade

from fastapi import APIRouter, Depends

import  os,sys
from datetime import  datetime  as dt
def create_table():

   path = db.RDB_PATH
   if not os.path.isfile(path):

      # テーブルを作成する
      db.Base.metadata.create_all(db.engine)

   # sample Uder
   admin = User(username='admin', password='test', mail='test@gmail.com')
   session  = db.SessionLocal()
   session.add(admin) 
   session.commit() 

   # Sample task 
   task = Task(
      model_name="Test005",
      train_start_date="20200101",
      train_end_date="20200107"
   )
   print(task)
   session.add(task)
   session.commit()

   # Sample task
   sample_dt = dt.now()
   task = Trade(
      symbol="BTC",
      event_datetime=sample_dt,
      price="123",
      size="321",
      ask="120",   
      bid="130",
   )
   print(task)
   session.add(task)
   session.commit()
   session.close()  
   
def delete_all():
   db.Base.metadata.drop_all(bind=db.engine)
   
if __name__ == "__main__":
   delete_all()
   create_table()