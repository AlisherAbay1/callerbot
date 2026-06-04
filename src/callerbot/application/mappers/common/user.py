from callerbot.application.dto.common import UserDTO
from callerbot.infrastructure.database.models import User


class UserMapper:
    @staticmethod
    def to_dto(model: User) -> UserDTO:
        user = UserDTO(
            tg_id=model.tg_id,
            is_globally_registered=model.is_globally_registered,
            global_emoji=model.global_emoji,
        )
        return user
