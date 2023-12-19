from pydantic import BaseModel, Field
from .base import Base


class Genre(BaseModel):

    genre_name: str = Field(alias="genreName")


class Author(BaseModel):

    full_name: str = Field(alias="fullName")


class Book(Base):

    title: str = Field(min_length=2)
    description: str
    year: int
    price: float
    author_id: int = Field(alias="authorId")
    genre_id: int = Field(alias="genreId")
    file_id: int = Field(alias="fileId")
