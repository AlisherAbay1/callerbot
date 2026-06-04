from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, VARCHAR
from callerbot.infrastructure.database.models.base import Base
from uuid import UUID
from uuid6 import uuid7
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from callerbot.infrastructure.database.models.chat_member import ChatMember


class User(Base, kw_only=True):
    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(default_factory=uuid7, primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    is_globally_registered: Mapped[bool] = mapped_column(default=False)
    global_emoji: Mapped[Optional[str]] = mapped_column(VARCHAR(16), nullable=True)

    chat_associations: Mapped[list["ChatMember"]] = relationship(
        lazy="noload", init=False, default_factory=list
    )
