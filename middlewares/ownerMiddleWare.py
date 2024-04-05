from starlette.middleware.base import BaseHTTPMiddleware
from exceptions.AllException import AccessDenied
from controllers.tokenProcessingController import get_user_by_name
from fastapi.responses import JSONResponse


class OwnerMiddleWare(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.request_counts = {}

    async def dispatch(self, request, call_next):
        login = request.state.user["login"]
        user = get_user_by_name(login)
        if user[2] != "owner":
            return JSONResponse(status_code=400, content={'reason': AccessDenied().reason})
        response = await call_next(request)
        return response
