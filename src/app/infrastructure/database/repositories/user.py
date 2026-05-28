from typing import Optional, Sequence
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from domain import User

class UserRepository:
    __slots__ = ("_session", )
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    