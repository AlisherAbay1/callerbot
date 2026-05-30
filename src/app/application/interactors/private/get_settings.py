from src.app.application.interfaces import UserRepositoryProtocol
from src.app.application.mappers.extended import UserMapperExtended


class GetSettingsInteractor:
    def __init__(self, user_repo: UserRepositoryProtocol) -> None:
        self.user_repo = user_repo

    async def __call__(self, tg_id: int):
        user = await self.user_repo.get_user_with_associations_and_chat_by_tg_id(tg_id)
        if user is None:
            raise
        dtos = UserMapperExtended.to_dto(user, user.chat_associations)
        return dtos
