from callerbot.application.interfaces import (
    UserRepositoryProtocol,
    UoWProtocol,
)


class UnSetEmojiGlobalyInteractor:
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
        user.global_emoji = None
        await self.uow.commit()
