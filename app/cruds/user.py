
from typing import List, Tuple, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker
import app.models.user as user_model
import app.schemas.user as user_schema
from sqlalchemy.engine import Result

def get_user(db:Session,user_id:int) -> user_model.User:
    """ Lookup user by user_id

    Returns:
        user_model.User
    """
    result =  db.query(user_model.User).filter(user_model.User.id==user_id).first()
    return result

def get_users(db:Session) -> List[Tuple[int, str, str, str, str]]:
    """ Lookup user by user_id

    Returns:
        user_model.User
    """
    result=(
        db.execute(
            select(
                user_model.User.id,
                user_model.User.username,
                user_model.User.password,
                user_model.User.mail
            )
        )
    )
    return result.all()

def create_user(
    db: Session, user_create: user_schema.UserCreate
        )  -> user_model.User:
    """ Create user
    Returns: 
        user_model.User
    """
    print(user_create.dict())
    user = user_model.User(**user_create.dict())
    print(user)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user(
    db: Session, user_create: user_schema.UserCreate, original: user_model.User
        ) -> user_model.User:    
    """ Create user
    Returns: 
        user_model.User
    """
    original.username = user_create.username
    original.password = user_create.password
    original.mail = user_create.mail
    
    db.add(original)
    db.commit()
    db.refresh(original)
    return original

def delete_user(db: Session, original: user_model.User) -> None:
    """ Delte user
    Args:
        db (Session): [description]
        original (user_model.User): [description]
    """
    db.delete(original)
    db.commit()