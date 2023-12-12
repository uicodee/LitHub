from datetime import datetime

from pydantic import BaseModel, Field


class Author(BaseModel):

    full_name: str = Field(alias="fullName")
    birth_date: datetime = Field(alias="birthDate")


class EditAuthor(Author):

    author_id: int = Field(alias="authorId")
