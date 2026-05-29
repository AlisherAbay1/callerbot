from src.app.application.interfaces import (
    UserRepositoryProtocol,
    TransactionAlchemyManagerProtocol,
)


class RegisterUserGlobalyInteractor:
    def __init__(
        self,
        repo: UserRepositoryProtocol,
        transaction: TransactionAlchemyManagerProtocol,
    ) -> None:
        self.repo = repo
        self.transaction = transaction

    async def __call__(self, tg_id: int):
        user = await self.repo.get_user_by_tg_id(tg_id)
        if user is None:
            raise
        user.is_globally_registered = True
        await self.transaction.commit()
