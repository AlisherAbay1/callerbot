from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from callerbot.infrastructure.database.models import Chat
from callerbot.application.interfaces import ChatRepositoryProtocol


class ChatRepository(ChatRepositoryProtocol):
    __slots__ = ("_session",)

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_chat_by_tg_id(self, tg_id: int) -> Optional[Chat]:
        stmt = select(Chat).where(Chat.tg_id == tg_id)
        chat = await self._session.scalar(stmt)
        return chat
