from pydantic import BaseModel, Field


class Genre(BaseModel):

    genre_name: str = Field(alias="genreName")


class Author(BaseModel):

    full_name: str = Field(alias="fullName")


class Book(BaseModel):

    title: str = Field(min_length=2)
    # author: list[Author] = Field(min_items=1)
    # genre: list[Genre] = Field(min_items=1)
    description: str
    year: int
    price: float
    author_id: int = Field(alias="authorId")
    genre_id: int = Field(alias="genreId")
    file_id: int = Field(alias="fileId")


class EditBook(Book):

    book_id: int = Field(alias="bookId", gt=0)
