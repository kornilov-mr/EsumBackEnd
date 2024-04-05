from fastapi import FastAPI
from starlette.requests import Request
from fastapi.responses import JSONResponse

from .AllException import TokenIsNotProvided, JWTTokenCheckException




def add_admit_exception_handler(api: FastAPI) -> None:
    @api.exception_handler(TokenIsNotProvided)
    async def unicorn_exception_handler(request: Request, exc: TokenIsNotProvided):
        return JSONResponse(
            status_code=400,
            content={"message": f"JWToken isn't provided"},
        )

    @api.exception_handler(JWTTokenCheckException)
    async def unicorn_exception_handler(request: Request, exc: JWTTokenCheckException):
        return JSONResponse(
            status_code=400,
            content={"message":"JWToken is not valid"},
        )



