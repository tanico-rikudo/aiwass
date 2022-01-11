from fastapi import APIRouter, Depends
from typing import List
# from sqlalchemy.ext.asyncio import AsyncSession
import app.schemas.user as user_schema
import app.cruds.task as user_crud
from sqlalchemy.orm import Session
from db.db import get_db


router = APIRouter()

@router.get("/users", response_model=List[user_schema.User])
async def list_users():
        return [user_schema.Task(id=1, model_id="sample model", 
                                 model_name="sample base model", status="unregistered")]


@router.post("/users", response_model=user_schema.UserCreateResponse)
async def create_user(user_body: user_schema.UserCreate, db: Session = Depends(get_db)
):
    return await user_crud.create_task(db, user_body)


@router.put("/users/{user_id}", response_model=user_schema.UserCreateResponse)
async def update_user(
    user_id: int, user_body: user_schema.UserCreate, db: Session = Depends(get_db)
):
    user = await user_crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return await user_crud.update_task(db, user_body, original=user)


@router.delete("/users/{user_id}", response_model=None)
async def delete_user(user_id: int):
    return