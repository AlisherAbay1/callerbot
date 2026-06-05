from callerbot.application.interfaces import (
    UserRepositoryProtocol,
    ChatMemberRepositoryProtocol,
    UoWProtocol,
    EmojiProtocol,
)


class RandomEmojiLocallyInteractor:
    def __init__(
        self,
        user_repo: UserRepositoryProtocol,
        chat_member_repo: ChatMemberRepositoryProtocol,
        uow: UoWProtocol,
        emoji: EmojiProtocol,
    ) -> None:
        self.user_repo = user_repo
        self.chat_member_repo = chat_member_repo
        self.uow = uow
        self.emoji = emoji

    async def __call__(self, user_tg_id: int):
        user = await self.user_repo.get_user_by_tg_id(user_tg_id)
        if user is None:
            raise
        chat_member = await self.chat_member_repo.get_chat_member_by_user_id(user.id)
        if chat_member is None:
            raise
        emoji = self.emoji.get_random_emoji()
        chat_member.emoji = emoji
        await self.uow.commit()
        return emoji
