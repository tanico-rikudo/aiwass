
from typing import List, Tuple, Optional

from sqlalchemy.ext.asyncio import AsyncSession

import app.models.user as user_model
import app.schemas.user as user_schema

async def get_user(db: AsyncSession, user_id: int) -> Optional[user_model.User]:
    """ Lookup user by user_id

    Returns:
        user_model.User
    """
    result: Result = await db.execute(
        select(user_model.User).filter(user_model.User.id == user_id)
    )
    user: Optional[Tuple[user_model.User]] = result.first()
    return user[0] if user is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す


async def create_user(
    db: AsyncSession, user_create: user_schema.UserCreate
        ) -> user_model.User:
    """ Create user
    Returns: 
        user_model.User
    """
    user = user_model.User(**user_create.dict())
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def update_user(
    db: AsyncSession, user_create: user_schema.UserCreate, original: user_model.User
        ) -> user_model.User:    
    """ Create user
    Returns: 
        user_model.User
    """
    original.model_name = user_create.model_name
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original

async def delete_user(db: AsyncSession, original: user_model.User) -> None:
    """ Delte user
    Args:
        db (AsyncSession): [description]
        original (user_model.User): [description]
    """
    await db.delete(original)
    await db.commit()