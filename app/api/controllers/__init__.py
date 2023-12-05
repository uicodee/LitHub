from fastapi import FastAPI
from .authentication import router as authentication_router
from .book import router as book_router


def setup(app: FastAPI) -> None:
    app.include_router(
        router=book_router,
        tags=["Book"]
    )
