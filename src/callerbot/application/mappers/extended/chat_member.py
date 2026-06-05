from callerbot.application.dto.extended import TagChatMembersDTO
from callerbot.infrastructure.database.models import ChatMember
from typing import Sequence


class ChatMembersMapperExtended:
    @staticmethod
    def to_tag_chat_members_dto(model: ChatMember) -> TagChatMembersDTO:
        dto = TagChatMembersDTO(user_tg_id=model.user.tg_id, user_emoji=model.emoji)
        return dto

    @staticmethod
    def to_tag_chat_members_dtos(
        models: Sequence[ChatMember],
    ) -> list[TagChatMembersDTO]:
        return [
            ChatMembersMapperExtended.to_tag_chat_members_dto(model) for model in models
        ]
