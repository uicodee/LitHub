from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.dao.rdb import BaseDAO, UserDAO, BookDAO, AuthorDAO, GenreDAO, FileDAO


class HolderDao:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.base = BaseDAO
        self.user = UserDAO(self.session)
        self.book = BookDAO(self.session)
        self.author = AuthorDAO(self.session)
        self.genre = GenreDAO(self.session)
        self.file = FileDAO(self.session)
