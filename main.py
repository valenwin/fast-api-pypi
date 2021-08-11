import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from views import home
from views import account
from views import packages

import os
import fastapi_jinja

dev_mode = True

folder = os.path.dirname(__file__)
template_folder = os.path.join(folder, 'templates')
template_folder = os.path.abspath(template_folder)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


def main():
    configure()
    uvicorn.run(app)


def configure():
    fastapi_jinja.global_init(template_folder, auto_reload=dev_mode)

    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


if __name__ == '__main__':
    main()
else:
    configure()
