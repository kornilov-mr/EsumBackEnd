import sys
sys.path.append('../routers')

from fastapi import FastAPI, Body, Header
from controllers.registrationController import (insert_user,
                                                check_if_name_already_exist)

from controllers.tokenProcessingController import get_user_by_name,create_new_access_JWToken,check_JTWToken

from exceptions.RegistrationException import (AlreadyExistedNameException,
                                              WrongNameException,
                                              WrongPasswordException,JWTTokenCheckException)
api = FastAPI()


@api.put("/registration/", status_code=201)
async def registrate_user(login: str = Body(), password: str = Body()):
    if check_if_name_already_exist(login) is True:
        raise AlreadyExistedNameException(login)
    token = await create_new_access_JWToken(login, password, "user")
    await insert_user(login, password)

    return {"message": "you have been successfully registered",
            "Token": token}


@api.put("/login/", status_code=200)
async def login_user(login: str = Body(), password: str = Body()):
    if check_if_name_already_exist(login) is not True:
        raise WrongNameException(login)

    login_found, password_found, role = get_user_by_name(login)
    if password_found != password:
        raise WrongPasswordException(password)

    return {"message": "you have been successfully authorized",
            "Token": create_new_access_JWToken(login, password, role)}


@api.get("/auth/", status_code=200)
async def authentication(token: str = Header()):
    token = check_JTWToken(token)
    if token is None:
        raise JWTTokenCheckException()
    return {"message": "you have been successfully authorized",
            "Token": token}



