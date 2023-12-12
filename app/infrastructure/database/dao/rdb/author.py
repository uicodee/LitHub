from pydantic import parse_obj_as
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app import dto
from app.api import schems
from app.infrastructure.database.dao.rdb import BaseDAO
from app.infrastructure.database.models import Author


class AuthorDAO(BaseDAO[Author]):
    def __init__(self, session: AsyncSession):
        super().__init__(Author, session)

    async def add_author(self, author: schems.Author) -> dto.Author:
        result = await self.session.execute(
            insert(Author).values(
                full_name=author.full_name,
                birth_date=author.birth_date
            ).returning(
                Author
            )
        )
        await self.session.commit()
        return dto.Author.from_orm(result.scalar())

    async def get_author(self, author_id: int) -> dto.Author:
        result = await self.session.execute(
            select(Author).where(Author.id == author_id)
        )
        author = result.scalar()
        if author is not None:
            return dto.Author.from_orm(author)

    async def get_authors(self) -> list[dto.Author]:
        result = await self.session.execute(
            select(Author)
        )
        return parse_obj_as(list[dto.Author], result.scalars().all())

    async def edit_author(self, author: schems.EditAuthor) -> dto.Author:
        result = await self.session.execute(
            update(Author).values(
                full_name=author.full_name,
                birth_date=author.birth_date
            ).where(Author.id == author.author_id).returning(
                Author
            )
        )
        await self.session.commit()
        return dto.Author.from_orm(result.scalar())

    async def delete_author(self, author_id: int) -> None:
        await self.session.execute(
            delete(Author).where(Author.id == author_id)
        )
        await self.session.commit()
