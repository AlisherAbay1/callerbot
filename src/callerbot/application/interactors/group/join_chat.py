from callerbot.application.interfaces import ChatRepositoryProtocol, UoWProtocol
from callerbot.infrastructure.database.models import Chat


class JoinChatInteractor:
    def __init__(self, repo: ChatRepositoryProtocol, uow: UoWProtocol) -> None:
        self.repo = repo
        self.uow = uow

    async def __call__(self, chat_tg_id: int, chat_title: str):
        chat = await self.repo.get_chat_by_tg_id(chat_tg_id)
        if chat is None:
            chat = Chat(tg_id=chat_tg_id, title=chat_title)
            await self.uow.add(chat)
        await self.uow.commit()
