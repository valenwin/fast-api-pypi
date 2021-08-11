import fastapi_jinja
from fastapi import Request, APIRouter

router = APIRouter()


@router.get('/account')
@fastapi_jinja.template('account/account.html')
def account(request: Request):
    return {
        "request": request
    }


@router.get('/account/login')
@fastapi_jinja.template('account/login.html')
def login(request: Request):
    return {
        "request": request
    }


@router.get('/account/logout')
@fastapi_jinja.template('account/logout.html')
def logout(request: Request):
    return {
        "request": request
    }


@router.get('/account/register')
@fastapi_jinja.template('account/register.html')
def register(request: Request):
    return {
        "request": request
    }
