from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, VARCHAR, ForeignKey
from src.app.domain.base import Base
from uuid import UUID
from uuid6 import uuid7

class UsersToChats(Base, kw_only=True):
    __tablename__ = "users_to_chats"

    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), primary_key=True)
    chat_id: Mapped[UUID] = mapped_column(ForeignKey("chat.id", ondelete="CASCADE"), primary_key=True)
    is_registered: Mapped[bool] = mapped_column(default=False)
    emoji: Mapped[str] = mapped_column(VARCHAR(16))