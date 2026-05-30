from typing import Optional
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.app.domain import User, UsersToChats


class UserRepository:
    __slots__ = ("_session",)

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_user_by_id(self, id: UUID) -> Optional[User]:
        user = await self._session.get(User, id)
        return user

    async def get_user_by_tg_id(self, tg_id: int) -> Optional[User]:
        stmt = select(User).where(User.tg_id == tg_id)
        user = await self._session.scalar(stmt)
        return user

    async def get_user_with_associations_and_chat_by_tg_id(
        self, tg_id: int
    ) -> Optional[User]:
        stmt = (
            select(User)
            .where(User.tg_id == tg_id)
            .options(selectinload(User.chat_associations).joinedload(UsersToChats.chat))
        )
        user = await self._session.scalar(stmt)
        return user
