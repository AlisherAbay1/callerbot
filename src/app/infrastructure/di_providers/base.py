from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncSession,
    create_async_engine,
    AsyncEngine,
)
from src.app.infrastructure.config import config
from collections.abc import AsyncGenerator
from src.app.infrastructure.database.transaction import TransactionAlchemyManager
from src.app.infrastructure.random_emoji import Emoji
from src.app.application.interfaces import (
    TransactionAlchemyManagerProtocol,
    EmojiProtocol,
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

    transaction = provide(
        TransactionAlchemyManager,
        scope=Scope.REQUEST,
        provides=TransactionAlchemyManagerProtocol,
    )
    emoji = provide(Emoji, scope=Scope.APP, provides=EmojiProtocol)
