import sys

sys.path.append('../routers')

from fastapi import FastAPI, Request
from controllers.ownerController import set_admin

from controllers.registrationController import check_if_name_already_exist

from exceptions.AllException import LoginDoesNotExist

api = FastAPI()


@api.put("/setAdmin/", status_code=201)
async def set_admin_route(request: Request):
    if check_if_name_already_exist(request.state.jsonBody["login"]) is False:
        raise LoginDoesNotExist()
    await set_admin(request.state.jsonBody["login"])
    return {"message": "Admit was successfully set"}
