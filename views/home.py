import fastapi_jinja
from fastapi import Request, APIRouter

from viewmodels.home.index_viewmodel import IndexViewModel

router = APIRouter()


@router.get('/')
@fastapi_jinja.template('home/index.html')
def index(request: Request):
    vm = IndexViewModel(request)
    return vm.to_dict()


@router.get('/about')
@fastapi_jinja.template('home/about.html')
def about(request: Request):
    return {
        "request": request
    }
