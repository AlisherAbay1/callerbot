from src.app.application.dto.common import ChatDTO
from src.app.domain import UsersToChats
from typing import Sequence


class ChatMapper:
    @staticmethod
    def to_dto(domain: UsersToChats) -> ChatDTO:
        # works only if Chat is joined
        chat = ChatDTO(
            tg_id=domain.chat.tg_id,
            is_registered=domain.is_registered,
            emoji=domain.emoji,
        )
        return chat

    @staticmethod
    def to_dtos(domains: Sequence[UsersToChats]) -> list[ChatDTO]:
        return [ChatMapper.to_dto(domain) for domain in domains]
