from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
import app.schemas.task as task_schema
import app.cruds.task as task_crud
from sqlalchemy.orm import Session
from db.db import get_db


router = APIRouter()

@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks(db: Session = Depends(get_db)):
    # return [task_schema.Task(id=1, model_id="sample model", 
    #                          model_name="sample base model", status="unregistered")]
    return await task_crud.get_tasks(db)

@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate, db:Session = Depends(get_db)
):
    return await task_crud.create_task(db, task_body)


@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(
    task_id: int, task_body: task_schema.TaskCreate, db: Session = Depends(get_db)
):
    task = await task_crud.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return await task_crud.update_task(db, task_body, original=task)


@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int):
    return


