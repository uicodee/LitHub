from datetime import datetime
from .base import Base

from pydantic import Field


class Author(Base):
    full_name: str = Field(alias="fullName")
    birth_date: datetime = Field(alias="birthDate")
