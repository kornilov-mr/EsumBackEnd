from starlette.middleware.base import BaseHTTPMiddleware

from fastapi.responses import JSONResponse
import json


class JSONParserMiddleWare(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.request_counts = {}

    async def dispatch(self, request, call_next):
        body = await request.body()
        jsonBody = json.loads(body)

        request.state.jsonBody = jsonBody
        response = await call_next(request)
        return response
