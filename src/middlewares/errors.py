from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware


class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except HTTPException as http_exception:
            return JSONResponse(
                status_code=http_exception.status_code,
                content={"detail": http_exception.detail},
            )
        except Exception as e:
            raise e

