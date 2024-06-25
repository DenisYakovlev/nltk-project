from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware


class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except HTTPException as http_exception:
            return JSONResponse(
                status_code=http_exception.status_code,
                content={"detail": http_exception.detail},
            )
        except Exception:
            return JSONResponse(
                status_code=500,
                content={"detail": "something went wrong ;("},
            )
