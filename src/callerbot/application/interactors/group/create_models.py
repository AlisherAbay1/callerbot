from callerbot.application.interfaces import (
    UoWProtocol,
    ChatRepositoryProtocol,
)
from callerbot.application.services import (
    GetOrCreateUserService,
    GetOrCreateChatMemberService,
)


class CreateModelsInteractor:
    def __init__(
        self,
        user_service: GetOrCreateUserService,
        chat_repo: ChatRepositoryProtocol,
        chat_member_service: GetOrCreateChatMemberService,
        uow: UoWProtocol,
    ) -> None:
        self.chat_repo = chat_repo
        self.user_service = user_service
        self.chat_member_service = chat_member_service
        self.uow = uow

    async def __call__(self, user_tg_id: int, chat_tg_id: int):
        user = await self.user_service(user_tg_id)
        chat = await self.chat_repo.get_chat_by_tg_id(chat_tg_id)
        if chat is None:
            raise
        chat_member = await self.chat_member_service(
            user_id=user.id,
            chat_id=chat.id,
            global_registration=user.is_globally_registered,
            global_emoji=user.global_emoji,
        )
        await self.uow.add(user)
        await self.uow.add(chat_member)
        await self.uow.commit()
