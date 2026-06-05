from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import VARCHAR, ForeignKey
from callerbot.infrastructure.database.models.base import Base
from uuid import UUID
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from callerbot.infrastructure.database.models.chat import Chat
    from callerbot.infrastructure.database.models.user import User


class ChatMember(Base, kw_only=True):
    __tablename__ = "chat_member"

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), primary_key=True
    )
    chat_id: Mapped[UUID] = mapped_column(
        ForeignKey("chat.id", ondelete="CASCADE"), primary_key=True
    )
    is_registered: Mapped[bool] = mapped_column(default=False)
    emoji: Mapped[str] = mapped_column(VARCHAR(16))

    chat: Mapped["Chat"] = relationship(init=False, lazy="noload", viewonly=True)
    user: Mapped["User"] = relationship(init=False, lazy="noload", viewonly=True)
