from pydantic import parse_obj_as
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app import dto
from app.api import schems
from app.infrastructure.database.dao.rdb import BaseDAO
from app.infrastructure.database.models import Book


class BookDAO(BaseDAO[Book]):
    def __init__(self, session: AsyncSession):
        super().__init__(Book, session)

    async def add_book(self, book: schems.Book) -> dto.Book:
        result = await self.session.execute(
            insert(Book).values(
                title=book.title,
                description=book.description,
                year=book.year,
                price=book.price
            ).returning(
                Book
            )
        )
        await self.session.commit()
        return dto.Book.from_orm(result.scalar())

    async def get_book(self, book_id: int) -> dto.Book:
        result = await self.session.execute(
            select(Book).where(Book.id == book_id)
        )
        book = result.scalar()
        if book is not None:
            return dto.Book.from_orm(book)

    async def get_books(self) -> list[dto.Book]:
        result = await self.session.execute(
            select(Book)
        )
        return parse_obj_as(list[dto.Book], result.scalars().all())

    async def edit_book(self, book: schems.EditBook) -> dto.Book:
        result = await self.session.execute(
            update(Book).values(
                title=book.title,
                description=book.description,
                year=book.year,
                price=book.price
            ).where(Book.id == book.book_id).returning(
                Book
            )
        )
        await self.session.commit()
        return dto.Book.from_orm(result.scalar())

    async def delete_book(self, book_id: int) -> None:
        await self.session.execute(
            delete(Book).where(Book.id == book_id)
        )
        await self.session.commit()
