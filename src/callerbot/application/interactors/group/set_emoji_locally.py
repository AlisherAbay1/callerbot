from callerbot.application.interfaces import (
    UserRepositoryProtocol,
    ChatMemberRepositoryProtocol,
    UoWProtocol,
)


class SetEmojiLocallyInteractor:
    def __init__(
        self,
        user_repo: UserRepositoryProtocol,
        chat_member_repo: ChatMemberRepositoryProtocol,
        uow: UoWProtocol,
    ) -> None:
        self.user_repo = user_repo
        self.chat_member_repo = chat_member_repo
        self.uow = uow

    async def __call__(self, tg_id: int, emoji: str):
        user = await self.user_repo.get_user_by_tg_id(tg_id)
        if user is None:
            raise
        chat_member = await self.chat_member_repo.get_chat_member_by_user_id(user.id)
        if chat_member is None:
            raise
        chat_member.emoji = emoji
        await self.uow.commit()
