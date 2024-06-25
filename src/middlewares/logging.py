from datetime import datetime
from typing import Callable

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from core import logger


class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: Callable) -> None:
        super().__init__(app)

    async def dispatch(
        self,
        request: Request,
        call_next: Callable[[Request], Response]
    ) -> Response:
        start_time = datetime.now()
        path = request.url.path

        logger.info(f"{request.method} {path}")

        response: Response = await call_next(request)

        end_time = datetime.now()
        process_time = (end_time - start_time).total_seconds() * 10000

        logger.info(
            f"{request.method} {response.status_code} {path} "
            f"completed in {int(process_time)} ms"
        )

        return response
