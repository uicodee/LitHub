from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.models import BaseModel


class File(BaseModel):

    __tablename__ = "file"

    path: Mapped[str] = mapped_column(String)
