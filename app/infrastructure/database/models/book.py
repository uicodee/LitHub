from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.models import BaseModel
# One To One (One2One)
# One To Many (One2Many)
# Many to Many (M2M)


class Book(BaseModel):

    __tablename__ = "book"

    title: Mapped[str] = mapped_column(String)
    # author: Mapped[str] = mapped_column(String)
    # genre: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    year: Mapped[int] = mapped_column(Integer)
    price: Mapped[float] = mapped_column(Float)