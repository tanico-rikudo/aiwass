from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates #templete



#fast api 
app = FastAPI(
    title='Aiwass',
    description='Middle Commander',
    version='0.9 beta'
)


# jinja
templates = Jinja2Templates(directory="templates")
jinja_env = templates.env

# def index(request: Request):
#     return {'Hello': 'World'}

def index(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request': request} )
    
def get_train_date(request: Request):
    return {'Hello': 'World'}
    
