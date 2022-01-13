from fastapi import FastAPI
from starlette.requests import Request
from sqlalchemy.orm import Session, sessionmaker
from db.db import SessionLocal
from app.routers import task, user

app = FastAPI()
app.include_router(task.router)
app.include_router(user.router)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response