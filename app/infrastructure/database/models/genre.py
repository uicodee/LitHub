from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.models import BaseModel


class Genre(BaseModel):

    __tablename__ = "genre"

    name: Mapped[str] = mapped_column(String)
