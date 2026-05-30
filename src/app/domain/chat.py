from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger
from src.app.domain.base import Base
from uuid import UUID
from uuid6 import uuid7
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.app.domain.user import User


class Chat(Base, kw_only=True):
    __tablename__ = "chat"

    id: Mapped[UUID] = mapped_column(primary_key=True, default_factory=uuid7)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)

    users: Mapped["User"] = relationship(
        secondary="users_to_chats", init=False, lazy="noload", default_factory=list
    )  # type: ignore
