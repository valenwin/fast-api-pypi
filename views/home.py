import fastapi_jinja
from fastapi import Request, APIRouter

router = APIRouter()


@router.get('/')
@fastapi_jinja.template('home/index.html')
def index(request: Request, username: str = 'Miles'):
    return {
        "request": request, "username": username
    }


@router.get('/about')
@fastapi_jinja.template('home/about.html')
def about(request: Request):
    return {
        "request": request
    }
