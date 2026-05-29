from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger
from src.app.domain.base import Base
from uuid import UUID
from uuid6 import uuid7


class Chat(Base, kw_only=True):
    __tablename__ = "chat"

    id: Mapped[UUID] = mapped_column(primary_key=True, default_factory=uuid7)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
