from fastapi import APIRouter, Depends
from typing import List
import app.schemas.task as task_schema
import app.cruds.task as task_crud
from sqlalchemy.orm import Session
from db.db import get_db

import app.models.task as task_model
from sqlalchemy import select

router = APIRouter()

@router.get("/tasks",response_model=List[task_schema.Task])
async def list_tasks(db: Session = Depends(get_db)):
    return task_crud.get_tasks(db)

@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate, db:Session = Depends(get_db)
):
    return task_crud.create_task(db, task_body)


@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(
    task_id: int, task_body: task_schema.TaskCreate, db: Session = Depends(get_db)
):
    task = task_crud.get_task(db, task_id=task_id)
    print(task)
    print(task_body)
    print("=======")
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task_crud.update_task(db, task_body, original=task)


@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = task_crud.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    print(task)
    return task_crud.delete_task(db, original=task)


