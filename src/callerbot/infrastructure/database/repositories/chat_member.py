from typing import Optional
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from callerbot.infrastructure.database.models import ChatMember
from callerbot.application.interfaces import ChatMemberRepositoryProtocol


class ChatMemberRepository(ChatMemberRepositoryProtocol):
    __slots__ = ("_session",)

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_chat_member_by_chat_id(self, tg_id: UUID) -> Optional[ChatMember]:
        stmt = select(ChatMember).where(ChatMember.chat_id == tg_id)
        chat_member = await self._session.scalar(stmt)
        return chat_member
