from sqlalchemy.ext.asyncio import AsyncSession
from src.app.domain import Base

class TransactionAlchemyManager:
    __slots__ = ("_session", )

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def commit(self) -> None:
        await self._session.commit()

    async def flush(self) -> None:
        await self._session.flush()

    async def save(self, model: Base) -> None:
        self._session.add(model)

    async def delete(self, model: Base) -> None:
        await self._session.delete(model)