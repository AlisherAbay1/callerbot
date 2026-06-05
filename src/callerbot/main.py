from callerbot.presentation.routes.private_router import router as private_common_router
from callerbot.presentation.routes.group_router import router as group_common_router
from aiogram import Dispatcher, Bot
from callerbot.infrastructure.config import config
from dishka import make_async_container
from dishka.integrations.aiogram import setup_dishka
from callerbot.infrastructure.di_providers import (
    BaseProvider,
    PrivateProvider,
    GroupProvider,
)
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

bot = Bot(token=config.telegram.bot_token.get_secret_value())
dispatcher = Dispatcher()
dispatcher.include_routers(private_common_router, group_common_router)

container = make_async_container(BaseProvider(), PrivateProvider(), GroupProvider())

setup_dishka(container=container, router=dispatcher, auto_inject=True)

dispatcher.shutdown.register(container.close)


async def on_startup():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(f"{config.telegram.webhooks_url}/webhook")


dispatcher.startup.register(on_startup)

app = web.Application()
SimpleRequestHandler(dispatcher=dispatcher, bot=bot).register(app, path="/webhook")
setup_application(app, dispatcher, bot=bot)
