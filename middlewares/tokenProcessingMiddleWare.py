from starlette.middleware.base import BaseHTTPMiddleware
from controllers.tokenProcessingController import check_JTWToken,read_pay_load
from exceptions.AllException import JWTTokenCheckException
from fastapi.responses import JSONResponse

class TokenProcessingMiddleWare(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.request_counts = {}

    async def dispatch(self, request, call_next):
        token = request.headers["brear"]
        token = check_JTWToken(token)
        if token is False:
            return JSONResponse(status_code=400,content={'reason': JWTTokenCheckException().reason})
        request.state.user = read_pay_load(token)
        response = await call_next(request)
        return response
