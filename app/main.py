from fastapi import FastAPI
from starlette.requests import Request
from sqlalchemy.orm import Session, sessionmaker
from db.db import SessionLocal
from app.routers import task, user, trade, web, orderbook

app = FastAPI(   
    title='AiwassAPI',
    description='Middle Commander',
    version='0.9 beta(^v^)')

app.include_router(task.router)
app.include_router(user.router)
app.include_router(trade.router)
app.include_router(web.router)
app.include_router(orderbook.router)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response

