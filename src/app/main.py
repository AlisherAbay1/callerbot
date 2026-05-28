from src.app.presentation.private_router import private_common_router
from aiogram import Dispatcher, Bot
from src.app.infrastructure.config import config
import asyncio
from dishka import make_async_container
from dishka.integrations.aiogram import setup_dishka
from src.app.infrastructure.di_providers import BaseProvider, PrivateProvider

bot = Bot(token=config.telegram.bot_token.get_secret_value())
dispatcher = Dispatcher()
dispatcher.include_routers(private_common_router)

container = make_async_container(
    BaseProvider(), 
    PrivateProvider()
)

setup_dishka(container=container, router=dispatcher, auto_inject=True)

dispatcher.shutdown.register(container.close)

async def start_polling():
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start_polling())
