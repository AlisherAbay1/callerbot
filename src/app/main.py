from src.app.presentation.private_router import private_common_router
from aiogram import Dispatcher, Bot
from src.app.infrastructure.config import config
import asyncio

bot = Bot(token=config.telegram.bot_token.get_secret_value())
dispatcher = Dispatcher()
dispatcher.include_routers(private_common_router)

async def start_polling():
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start_polling())