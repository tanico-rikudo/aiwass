from fastapi import APIRouter, Depends
from typing import List
import app.schemas.user as user_schema
import app.cruds.user as user_crud
from sqlalchemy.orm import Session
from db.db import get_db

import app.models.user as user_model
from sqlalchemy import select

router = APIRouter()

@router.get("/users",response_model=List[user_schema.User])
async def list_users(db: Session = Depends(get_db)):
    return user_crud.get_users(db)

@router.post("/users", response_model=user_schema.UserCreateResponse)
async def create_user(user_body: user_schema.UserCreate, db:Session = Depends(get_db)
):
    return user_crud.create_user(db, user_body)


@router.put("/users/{user_id}", response_model=user_schema.UserCreateResponse)
async def update_user(
    user_id: int, user_body: user_schema.UserCreate, db: Session = Depends(get_db)
):
    user = user_crud.get_user(db, user_id=user_id)
    print(user)
    print(user_body)
    print("=======")
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user_crud.update_user(db, user_body, original=user)


@router.delete("/users/{user_id}", response_model=None)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    print(user)
    return user_crud.delete_user(db, original=user)


