from src.app.domain import User
from src.app.application.interfaces import TransactionAlchemyManagerProtocol, UserRepositoryProtocol

class StartInteractor:
    def __init__(self, 
                 repo: UserRepositoryProtocol,
                 transaction: TransactionAlchemyManagerProtocol) -> None:
        self.repo = repo
        self.transaction = transaction

    async def __call__(self,tg_id: int):
        user = await self.repo.get_user_by_tg_id(tg_id)
        if user is None:
            new_user = User(
                tg_id=tg_id, 
                global_emoji=None
            )
            await self.transaction.save(new_user)
        await self.transaction.commit()