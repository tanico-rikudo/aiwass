from fastapi import APIRouter, Depends
from typing import List
import app.schemas.task as task_schema
import app.cruds.task as task_crud
from app.db.db import get_db


router = APIRouter()

@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks():
        return [task_schema.Task(id=1, model_id="sample model", 
                                 model_name="sample base model", status="unregistered")]

@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
):
    return await task_crud.create_task(db, task_body)


@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=task_id, **task_body.dict())


@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int):
    return