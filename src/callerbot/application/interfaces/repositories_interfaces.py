from callerbot.infrastructure.database.models import User, Chat, ChatMember
from typing import Protocol, Optional, Sequence

from uuid import UUID


class UserRepositoryProtocol(Protocol):
    async def get_user_by_id(self, id: UUID) -> Optional[User]: ...
    async def get_user_by_tg_id(self, tg_id: int) -> Optional[User]: ...
    async def get_user_with_associations_and_chat_by_tg_id(
        self, tg_id: int
    ) -> Optional[User]: ...


class ChatRepositoryProtocol(Protocol):
    async def get_chat_by_tg_id(self, tg_id: int) -> Optional[Chat]: ...


class ChatMemberRepositoryProtocol(Protocol):
    async def get_chat_member_by_user_id(self, tg_id: UUID) -> Optional[ChatMember]: ...
    async def get_registred_chat_members_by_chat_id(
        self, chat_id: UUID
    ) -> Sequence[ChatMember]: ...
