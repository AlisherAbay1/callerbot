from callerbot.application.interfaces import (
    UserRepositoryProtocol,
    ChatMemberRepositoryProtocol,
    ChatRepositoryProtocol,
)
from callerbot.application.mappers.extended import ChatMembersMapperExtended
from callerbot.application.dto.extended import TagChatMembersDTO


class GetRegistredChatMembersInteractor:
    def __init__(
        self,
        user_repo: UserRepositoryProtocol,
        chat_repo: ChatRepositoryProtocol,
        chat_member_repo: ChatMemberRepositoryProtocol,
    ) -> None:
        self.user_repo = user_repo
        self.chat_repo = chat_repo
        self.chat_member_repo = chat_member_repo

    async def __call__(self, chat_tg_id: int) -> list[TagChatMembersDTO]:
        chat = await self.chat_repo.get_chat_by_tg_id(chat_tg_id)
        if chat is None:
            raise
        chat_members = (
            await self.chat_member_repo.get_registred_chat_members_by_chat_id(chat.id)
        )
        return ChatMembersMapperExtended.to_tag_chat_members_dtos(chat_members)
