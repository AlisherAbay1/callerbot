from collections.abc import Awaitable
from typing import Any, Callable

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

from callerbot.application.interactors.group import CreateModelsInteractor


class GroupMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        if isinstance(event, Message):
            if event.chat.type not in ("group", "supergroup"):
                print("Middleware ignored")
                return await handler(event, data)
            container = data.get("dishka_container")
            if container is None:
                raise
            assert event.from_user
            interactor: CreateModelsInteractor = await container.get(
                CreateModelsInteractor
            )
            await interactor(user_tg_id=event.from_user.id, chat_tg_id=event.chat.id)
            print("Middleware worked")
        return await handler(event, data)
