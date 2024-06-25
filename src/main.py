from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from core import init_nltk, logger, settings
from middlewares import LoggingMiddleware, ErrorHandlerMiddleware
from routers import ping_router


@asynccontextmanager
async def lifespan(app):
    # on startup

    logger.info("Starting server...")
    init_nltk()

    yield
    # on shutdown

    logger.info("Shuting down server...")


app = FastAPI(lifespan=lifespan)

# add middlewares here
app.add_middleware(LoggingMiddleware)
app.add_middleware(ErrorHandlerMiddleware)

# add routers here
app.include_router(ping_router, prefix="")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=settings.PORT,
        log_config=settings.LOGGING_CONFIG,
        reload=settings.DEBUG,
    )
