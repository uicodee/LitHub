from pydantic import parse_obj_as
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app import dto
from app.api import schems
from app.infrastructure.database.dao.rdb import BaseDAO
from app.infrastructure.database.models import Genre


class GenreDAO(BaseDAO[Genre]):
    def __init__(self, session: AsyncSession):
        super().__init__(Genre, session)

    async def add_genre(self, genre: schems.Genre) -> dto.Genre:
        result = await self.session.execute(
            insert(Genre).values(
                name=genre.name
            ).returning(
                Genre
            )
        )
        await self.session.commit()
        return dto.Genre.from_orm(result.scalar())

    async def get_genre(self, genre_id: int) -> dto.Genre:
        result = await self.session.execute(
            select(Genre).where(Genre.id == genre_id)
        )
        genre = result.scalar()
        if genre is not None:
            return dto.Genre.from_orm(genre)

    async def get_genres(self) -> list[dto.Genre]:
        result = await self.session.execute(
            select(Genre)
        )
        return parse_obj_as(list[dto.Genre], result.scalars().all())

    async def edit_genre(self, genre: schems.EditGenre) -> dto.Genre:
        result = await self.session.execute(
            update(Genre).values(
                name=genre.name
            ).where(Genre.id == genre.genre_id).returning(
                Genre
            )
        )
        await self.session.commit()
        return dto.Genre.from_orm(result.scalar())

    async def delete_genre(self, genre_id: int) -> None:
        await self.session.execute(
            delete(Genre).where(Genre.id == genre_id)
        )
        await self.session.commit()
