# from urls import app
import uvicorn


from fastapi import FastAPI
from app.routers import task, user

app = FastAPI()
app.include_router(task.router)
app.include_router(user.router)

if __name__ == '__main__':
    # コンソールで [$ uvicorn run:app --reload]でも可
    uvicorn.run(app="app.main:app", port=3018,reload=True, access_log=True)