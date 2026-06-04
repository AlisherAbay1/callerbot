from callerbot.application.interfaces import UserRepositoryProtocol
from callerbot.infrastructure.database.models import User


class GetOrCreateUserService:
    def __init__(self, repo: UserRepositoryProtocol) -> None:
        self.repo = repo

    async def __call__(self, tg_id: int) -> User:
        user = await self.repo.get_user_by_tg_id(tg_id)
        if user is None:
            user = User(tg_id=tg_id, global_emoji=None)
        return user
