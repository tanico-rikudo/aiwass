from fastapi import APIRouter
from typing import List
import app.schemas.user as user_schema

router = APIRouter()


@router.get("/users")
async def list_users():
    pass

@router.post("/users")
async def create_user():
    pass


@router.put("/users/{user_id}")
async def update_user():
    pass


@router.delete("/users/{user_id}")
async def delete_user():
    pass