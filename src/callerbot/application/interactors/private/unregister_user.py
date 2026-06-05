from callerbot.application.interfaces import (
    UserRepositoryProtocol,
    UoWProtocol,
)


class UnRegisterUserGlobalyInteractor:
    def __init__(
        self,
        repo: UserRepositoryProtocol,
        uow: UoWProtocol,
    ) -> None:
        self.repo = repo
        self.uow = uow

    async def __call__(self, user_tg_id: int):
        user = await self.repo.get_user_by_tg_id(user_tg_id)
        if user is None:
            raise
        user.is_globally_registered = False
        await self.uow.commit()
