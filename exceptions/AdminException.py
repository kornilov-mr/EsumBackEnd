from fastapi import FastAPI
from starlette.requests import Request
from fastapi.responses import JSONResponse

from .AllException import AccessDenied,AdminKeyIsNotProvided,JWTTokenCheckException


def add_admin_exception_handler(api: FastAPI) -> None:
    @api.exception_handler(AccessDenied)
    async def unicorn_exception_handler(request: Request, exc: AccessDenied):
        print("test")
        return JSONResponse(
            status_code=403,
            content={"message": "user isn't admin"},
        )

    @api.exception_handler(AdminKeyIsNotProvided)
    async def unicorn_exception_handler(request: Request, exc: AdminKeyIsNotProvided):
        return JSONResponse(
            status_code=400,
            content={"message": "admin key isn't provided"},
        )

    @api.exception_handler(JWTTokenCheckException)
    async def unicorn_exception_handler(request: Request, exc: JWTTokenCheckException):
        return JSONResponse(
            status_code=400,
            content={"message": "JWToken is not valid"},
        )
