from src.app.application.interfaces import (
    UserRepositoryProtocol,
    TransactionAlchemyManagerProtocol,
)


class SetEmojiGlobalyInteractor:
    def __init__(
        self,
        repo: UserRepositoryProtocol,
        transaction: TransactionAlchemyManagerProtocol,
    ) -> None:
        self.repo = repo
        self.transaction = transaction

    async def __call__(self, tg_id: int, emoji: str):
        user = await self.repo.get_user_by_tg_id(tg_id)
        if user is None:
            raise
        user.global_emoji = emoji
        await self.transaction.commit()
