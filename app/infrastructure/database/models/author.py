from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.models import BaseModel


class Author(BaseModel):

    __tablename__ = "author"

    full_name: Mapped[str] = mapped_column(String)
    birth_date: Mapped[datetime] = mapped_column(DateTime(True))