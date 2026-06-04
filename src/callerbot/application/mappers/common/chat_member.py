from callerbot.application.dto.common import ChatMemberDTO
from callerbot.infrastructure.database.models import ChatMember
from typing import Sequence


class ChatMemberMapper:
    @staticmethod
    def to_dto(model: ChatMember) -> ChatMemberDTO:
        # works only if Chat is joined
        chat = ChatMemberDTO(
            tg_id=model.chat.tg_id,
            chat_title=model.chat.title,
            is_registered=model.is_registered,
            emoji=model.emoji,
        )
        return chat

    @staticmethod
    def to_dtos(models: Sequence[ChatMember]) -> list[ChatMemberDTO]:
        return [ChatMemberMapper.to_dto(model) for model in models]
