from callerbot.application.dto.extended import UserWithChatsDTO
from callerbot.infrastructure.database.models import User, ChatMember
from typing import Sequence
from callerbot.application.mappers.common import ChatMemberMapper


class UserMapperExtended:
    @staticmethod
    def to_dto(model: User, models: Sequence[ChatMember]) -> UserWithChatsDTO:
        user = UserWithChatsDTO(
            tg_id=model.tg_id,
            is_globally_registered=model.is_globally_registered,
            global_emoji=model.global_emoji,
            chats=ChatMemberMapper.to_dtos(models),
        )
        return user
