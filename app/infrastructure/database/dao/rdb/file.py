from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app import dto
from app.infrastructure.database.dao.rdb import BaseDAO
from app.infrastructure.database.models import File


class FileDAO(BaseDAO[File]):
    def __init__(self, session: AsyncSession):
        super().__init__(File, session)

    async def add_file(self, path: str) -> dto.File:
        result = await self.session.execute(
            insert(File).values(path=path).returning(
                File
            )
        )
        await self.session.commit()
        return dto.File.from_orm(result.scalar())
