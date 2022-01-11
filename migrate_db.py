import db.db as db
from  app.models import * 
from  app.models.user import User
from  app.models.task import Task

import  os,sys
def create_table():

   path = db.RDB_PATH
   if not os.path.isfile(path):

      # テーブルを作成する
      db.Base.metadata.create_all(db.engine)

   # sample Uder
   admin = User(username='admin', password='test', mail='test@gmail.com')
   session  = db.Session()
   session.add(admin) 
   session.commit() 

   # Sample task 
   task = Task(
      model_name="Test005",
      TRAIN_START_DATE="20200101",
      TRAIN_END_DATE="20200107",
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