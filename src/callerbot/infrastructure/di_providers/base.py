from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncSession,
    create_async_engine,
    AsyncEngine,
)
from callerbot.infrastructure.config import config
from collections.abc import AsyncGenerator
from callerbot.infrastructure.database.uow import UoW
from callerbot.infrastructure.random_emoji import Emoji
from callerbot.infrastructure.database.repositories import (
    UserRepository,
    ChatRepository,
    ChatMemberRepository,
)
from callerbot.application.interfaces import (
    UoWProtocol,
    EmojiProtocol,
    UserRepositoryProtocol,
    ChatMemberRepositoryProtocol,
    ChatRepositoryProtocol,
)


class BaseProvider(Provider):
    @provide(scope=Scope.APP)
    async def get_db_engine(self) -> AsyncGenerator[AsyncEngine, None]:
        engine = create_async_engine(url=config.database.get_url)
        yield engine
        await engine.dispose()

    @provide(scope=Scope.APP)
    async def get_db_session_maker(
        self, engine: AsyncEngine
    ) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(bind=engine)

    @provide(scope=Scope.REQUEST)
    async def get_db_session(
        self, session_maker: async_sessionmaker[AsyncSession]
    ) -> AsyncGenerator[AsyncSession, None]:
        async with session_maker() as session:
            yield session

    uow = provide(
        UoW,
        scope=Scope.REQUEST,
        provides=UoWProtocol,
    )
    emoji = provide(Emoji, scope=Scope.APP, provides=EmojiProtocol)
    user_repository = provide(
        UserRepository, provides=UserRepositoryProtocol, scope=Scope.REQUEST
    )
    chat_repository = provide(
        ChatRepository, provides=ChatRepositoryProtocol, scope=Scope.REQUEST
    )
    chat_member_repository = provide(
        ChatMemberRepository, provides=ChatMemberRepositoryProtocol, scope=Scope.REQUEST
    )
