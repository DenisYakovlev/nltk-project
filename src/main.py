from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from core import init_nltk, logger, settings
from middlewares import LoggingMiddleware, ErrorHandlerMiddleware
from routers import nltk_router


@asynccontextmanager
async def lifespan(app):
    # on startup

    logger.info(f"Starting server on port {settings.PORT}...")
    init_nltk()

    yield
    # on shutdown

    logger.info("Shutting down server...")


app = FastAPI(lifespan=lifespan)

# add middlewares here
app.add_middleware(LoggingMiddleware)
app.add_middleware(ErrorHandlerMiddleware)

# add routers here
app.include_router(nltk_router, prefix="")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.PORT,
        log_config=settings.LOGGING_CONFIG,
        reload=settings.DEBUG,
    )
