from callerbot.application.interfaces import (
    UserRepositoryProtocol,
    UoWProtocol,
)


class SetEmojiGlobalyInteractor:
    def __init__(
        self,
        repo: UserRepositoryProtocol,
        uow: UoWProtocol,
    ) -> None:
        self.repo = repo
        self.uow = uow

    async def __call__(self, tg_id: int, emoji: str):
        user = await self.repo.get_user_by_tg_id(tg_id)
        if user is None:
            raise
        user.global_emoji = emoji
        await self.uow.commit()
