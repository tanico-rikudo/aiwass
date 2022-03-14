from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

@router.get("/index", response_class=HTMLResponse)
async def read_index(request: Request):
    print("=======")
    return templates.TemplateResponse("index.html", {"request": request})
