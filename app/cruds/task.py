
from typing import List, Tuple, Optional

from sqlalchemy.ext.asyncio import AsyncSession

import app.models.task as task_model
import app.schemas.task as task_schema

async def get_tasks(db: AsyncSession) -> List[Tuple[int, str, str]]:
    """ Lookup task by task_id

    Returns:
        task_model.Task
    """
    result: Result = await (
        db.execute(
            select(
                task_model.Task.id,
                task_model.Task.model_id,
                task_model.Task.model_name
            )
        )
    )
    return result.all()

async def create_task(
    db: AsyncSession, task_create: task_schema.TaskCreate
        ) -> task_model.Task:
    """ Create task
    Returns: 
        task_model.Task
    """
    task = task_model.Task(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

async def update_task(
    db: AsyncSession, task_create: task_schema.TaskCreate, original: task_model.Task
        ) -> task_model.Task:    
    """ Create task
    Returns: 
        task_model.Task
    """
    original.model_name = task_create.model_name
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original

async def delete_task(db: AsyncSession, original: task_model.Task) -> None:
    """ Delte task
    Args:
        db (AsyncSession): [description]
        original (task_model.Task): [description]
    """
    await db.delete(original)
    await db.commit()