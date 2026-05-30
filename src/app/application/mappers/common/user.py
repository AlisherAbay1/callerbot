from src.app.application.dto.common import UserDTO
from src.app.domain import User


class UserMapper:
    @staticmethod
    def to_dto(domain: User) -> UserDTO:
        user = UserDTO(
            tg_id=domain.tg_id,
            is_globally_registered=domain.is_globally_registered,
            global_emoji=domain.global_emoji,
        )
        return user
