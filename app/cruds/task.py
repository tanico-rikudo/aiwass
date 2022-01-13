
from typing import List, Tuple, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker
import app.models.task as task_model
import app.schemas.task as task_schema
from sqlalchemy.engine import Result

def get_task(db:Session,task_id:int) -> task_model.Task:
    """ Lookup task by task_id

    Returns:
        task_model.Task
    """
    result =  db.query(task_model.Task).filter(task_model.Task.id==task_id).first()
    return result

def get_tasks(db:Session) -> List[Tuple[int, str, str, str, str]]:
    """ Lookup task by task_id

    Returns:
        task_model.Task
    """
    result=(
        db.execute(
            select(
                task_model.Task.id,
                task_model.Task.model_id,
                task_model.Task.model_name,
                task_model.Task.train_start_date,
                task_model.Task.train_end_date
            )
        )
    )
    return result.all()

def create_task(
    db: Session, task_create: task_schema.TaskCreate
        )  -> task_model.Task:
    """ Create task
    Returns: 
        task_model.Task
    """
    task = task_model.Task(**task_create.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def update_task(
    db: Session, task_create: task_schema.TaskCreate, original: task_model.Task
        ) -> task_model.Task:    
    """ Create task
    Returns: 
        task_model.Task
    """
    original.model_id = task_create.model_id
    original.model_name = task_create.model_name
    original.train_start_date = task_create.train_start_date
    original.train_end_date = task_create.train_end_date
    
    db.add(original)
    db.commit()
    db.refresh(original)
    return original

def delete_task(db: Session, original: task_model.Task) -> None:
    """ Delte task
    Args:
        db (Session): [description]
        original (task_model.Task): [description]
    """
    print("dffffff~==========")
    db.delete(original)
    db.commit()