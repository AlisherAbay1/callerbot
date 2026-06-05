from typing import Optional, Sequence
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from callerbot.infrastructure.database.models import ChatMember
from callerbot.application.interfaces import ChatMemberRepositoryProtocol


class ChatMemberRepository(ChatMemberRepositoryProtocol):
    __slots__ = ("_session",)

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_chat_member_by_user_id(self, tg_id: UUID) -> Optional[ChatMember]:
        stmt = select(ChatMember).where(ChatMember.user_id == tg_id)
        chat_member = await self._session.scalar(stmt)
        return chat_member

    async def get_registred_chat_members_by_chat_id(
        self, chat_id: UUID
    ) -> Sequence[ChatMember]:
        stmt = (
            select(ChatMember)
            .where(ChatMember.chat_id == chat_id, ChatMember.is_registered == True)  # noqa: E712
            .options(joinedload(ChatMember.user))
        )
        chat_members = await self._session.scalars(stmt)
        return chat_members.all()
