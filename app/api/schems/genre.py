from pydantic import BaseModel, Field


class Genre(BaseModel):

    name: str


class EditGenre(Genre):

    genre_id: int = Field(alias="genreId")

