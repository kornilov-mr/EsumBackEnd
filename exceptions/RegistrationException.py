from fastapi import FastAPI
from starlette.requests import Request
from fastapi.responses import JSONResponse

from .AllException import (NotValidNameException,
                          NotValidPasswordException,
                          AlreadyExistedNameException,
                          WrongPasswordException,
                          WrongNameException,
                          JWTTokenCheckException)



def add_user_registration_handler(api: FastAPI) -> None:
    @api.exception_handler(NotValidNameException)
    async def unicorn_exception_handler(request: Request, exc: NotValidNameException):
        return JSONResponse(
            status_code=400,
            content={"message": f"Invalid login: {exc.login}"},
        )

    @api.exception_handler(NotValidPasswordException)
    async def unicorn_exception_handler(request: Request, exc: NotValidPasswordException):
        return JSONResponse(
            status_code=400,
            content={"message": f"Invalid password: {exc.password}"},
        )

    @api.exception_handler(AlreadyExistedNameException)
    async def unicorn_exception_handler(request: Request, exc: AlreadyExistedNameException):
        return JSONResponse(
            status_code=400,
            content={"message": f"login already exist: {exc.login}"},
        )

    @api.exception_handler(WrongPasswordException)
    async def unicorn_exception_handler(request: Request, exc: WrongPasswordException):
        return JSONResponse(
            status_code=400,
            content={"message": f"Wrong password: {exc.password}"},
        )

    @api.exception_handler(WrongNameException)
    async def unicorn_exception_handler(request: Request, exc: WrongNameException):
        return JSONResponse(
            status_code=400,
            content={"message": f"Wrong login: {exc.login}"},
        )

    @api.exception_handler(JWTTokenCheckException)
    async def unicorn_exception_handler(request: Request, exc: JWTTokenCheckException):
        return JSONResponse(
            status_code=400,
            content={"message": "JWToken is not valid"},
        )




