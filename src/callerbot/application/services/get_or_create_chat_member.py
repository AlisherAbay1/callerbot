from callerbot.application.interfaces import ChatMemberRepositoryProtocol, EmojiProtocol
from callerbot.infrastructure.database.models import ChatMember
from uuid import UUID
from typing import Optional


class GetOrCreateChatMemberService:
    def __init__(
        self, repo: ChatMemberRepositoryProtocol, emoji: EmojiProtocol
    ) -> None:
        self.repo = repo
        self.emoji = emoji

    async def __call__(
        self, user_id: UUID, chat_id: UUID, global_emoji: Optional[str]
    ) -> ChatMember:
        chat_member = await self.repo.get_chat_member_by_chat_id(chat_id)
        if chat_member is None:
            chat_member = ChatMember(
                user_id=user_id,
                chat_id=chat_id,
                is_registered=True,
                emoji=global_emoji or self.emoji.get_random_emoji(),
            )
        return chat_member
