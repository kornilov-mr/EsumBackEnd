from fastapi import FastAPI

from routers.index import subApp
from middlewares.adminMiddleWare import AdminMiddleWare

app = FastAPI()

app.mount("/backEnd", subApp)




