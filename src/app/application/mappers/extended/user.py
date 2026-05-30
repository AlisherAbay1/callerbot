from src.app.application.dto.extended import UserWithChatsDTO
from src.app.domain import User, UsersToChats
from typing import Sequence
from src.app.application.mappers.common import ChatMapper


class UserMapperExtended:
    @staticmethod
    def to_dto(domain: User, domains: Sequence[UsersToChats]) -> UserWithChatsDTO:
        user = UserWithChatsDTO(
            tg_id=domain.tg_id,
            is_globally_registered=domain.is_globally_registered,
            global_emoji=domain.global_emoji,
            chats=ChatMapper.to_dtos(domains),
        )
        return user
