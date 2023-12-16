from fastapi import FastAPI
from .authentication import router as authentication_router
from .book import router as book_router
from .author import router as author_router
from .genre import router as genre_router


def setup(app: FastAPI) -> None:
    app.include_router(
        router=book_router,
        tags=["Book"]
    )
    app.include_router(
        router=author_router,
        tags=["Author"]
    )
    app.include_router(
        router=genre_router,
        tags=["Genre"]
    )
