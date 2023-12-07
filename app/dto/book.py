from pydantic import BaseModel, Field
from .base import Base


class Genre(BaseModel):

    genre_name: str = Field(alias="genreName")


class Author(BaseModel):

    full_name: str = Field(alias="fullName")


class Book(Base):

    title: str = Field(min_length=2)
    # author: list[Author] = Field(min_items=1)
    # genre: list[Genre] = Field(min_items=1)
    description: str
    year: int
    price: float
