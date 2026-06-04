from callerbot.infrastructure.database.models import User
from callerbot.application.interfaces import (
    UoWProtocol,
    UserRepositoryProtocol,
)


class StartInteractor:
    def __init__(
        self,
        repo: UserRepositoryProtocol,
        uow: UoWProtocol,
    ) -> None:
        self.repo = repo
        self.uow = uow

    async def __call__(self, tg_id: int):
        user = await self.repo.get_user_by_tg_id(tg_id)
        if user is None:
            new_user = User(tg_id=tg_id, global_emoji=None)
            await self.uow.add(new_user)
        await self.uow.commit()
