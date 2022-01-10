import db
from   app.db import Base,RDB_PATH,engine
from  models import * 
import  os,sys
def create_table():

   path = db.RDB_PATH
   if not os.path.isfile(path):

      # テーブルを作成する
      Base.metadata.create_all(db.engine)

   # sample Uder
   admin = User(username='admin', password='test', mail='test@gmail.com')
   db.session.add(admin) 
   db.session.commit() 

   # Sample task 
   task = Task(
      model_name="Test005",
      TRAIN_START_DATE="20200101",
      TRAIN_END_DATE="20200107",
   )
   print(task)
   db.session.add(task)
   db.session.commit()
   db.session.close()  
   
def delete_all():
   Base.metadata.drop_all(bind=engine)
   
if __name__ == "__main__":
   delete_all()
   create_table()