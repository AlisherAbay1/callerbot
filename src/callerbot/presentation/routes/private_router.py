from aiogram import Router, F
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.types import Message
import inspect
from dishka import FromDishka
from callerbot.application.interactors.private import (
    StartInteractor,
    RegisterUserGlobalyInteractor,
    UnRegisterUserGlobalyInteractor,
    SetEmojiGlobalyInteractor,
    UnSetEmojiGlobalyInteractor,
    GetSettingsInteractor,
)
from emoji import is_emoji, emoji_count

router = Router(name="privat common router")
router.message.filter((F.chat.type == "private") & F.from_user)


@router.message(CommandStart())
async def start(message: Message, interactor: FromDishka[StartInteractor]):
    assert message.from_user
    await interactor(message.from_user.id)
    text = """
            Привет!
            Я бот, который будет тегать всех зарегистрировавшихся юзеров.
            Список команд для чата:
            /all - тегает всех юзеров, которые дали на  это согласие. 
            /reg - регистрирует вас в список вызываемых юзеров. 
            /unreg - убирает вас в список вызываемых юзеров.
            /setme (emoji) - устанавливает эмодзи. 
            /unsetme (emoji) - убирает эмодзи. 
            ПШЕ
            Список команд для личных сообщений:
            /reg - вы будете зарегистрированы во всех чатах по дефолту. 
            /unreg - вас уберут из регистрации во всех чатах по дефолту. 
            /setme (emoji) - устанавливает глобальный эмодзи.
            /unsetme - убирает глобальный эмодзи.
            /getsettings - вы увидите свои настройки. Глобальные и локальные. 

            В личных сообщениях вы можете выбрать глобальный параметр регистации, 
            однако локальные параметры регистрации имеют больший приоритет. 
            Аналогичная ситуация с emoji. 
           """
    await message.answer(inspect.cleandoc(text))


@router.message(Command("reg"))
async def reg_globally(
    message: Message, interactor: FromDishka[RegisterUserGlobalyInteractor]
):
    assert message.from_user
    await interactor(message.from_user.id)
    await message.answer("Вы установили глобальную регистрацию.")


@router.message(Command("unreg"))
async def unreg_globally(
    message: Message, interactor: FromDishka[UnRegisterUserGlobalyInteractor]
):
    assert message.from_user
    await interactor(message.from_user.id)
    await message.answer("Вы убрали глобальную регистрацию.")


@router.message(Command("setme"))
async def setme_globally(
    message: Message,
    command: CommandObject,
    interactor: FromDishka[SetEmojiGlobalyInteractor],
):
    assert message.from_user
    text = command.args
    if text is None:
        await message.answer("Вы должны передать смайлик.")
        return
    if not (is_emoji(text) and emoji_count(text) == 1):
        await message.answer("Передайте эмодзи.")
        return
    await interactor(message.from_user.id, text)
    await message.answer(f"Вы установили глобальный эмодзи: {text}")


@router.message(Command("unsetme"))
async def unsetme_globally(
    message: Message,
    interactor: FromDishka[UnSetEmojiGlobalyInteractor],
):
    assert message.from_user
    await interactor(message.from_user.id)
    await message.answer("Вы убрали глобальный эмодзи")


@router.message(Command("getsettings"))
async def getsettings(
    message: Message,
    interactor: FromDishka[GetSettingsInteractor],
):
    assert message.from_user
    dto = await interactor(message.from_user.id)
    global_settings = f"""
                Глобальные настройки:
                Глобальная регистрация: {["Выключена", "Включена"][dto.is_globally_registered]}
                Глобальное эмодзи: {"Нету" if dto.global_emoji is None else dto.global_emoji}
                """
    await message.answer(inspect.cleandoc(global_settings))
    local_settings = ["Локальные настройки:"] + [
        inspect.cleandoc(f"""
                           Название чата: {chat.chat_title}
                           Локальная регистрация: {["Выключена", "Включена"][chat.is_registered]}
                           Локальное эмодзи: {"Нету" if chat.emoji is None else chat.emoji}
                          """)
        for chat in dto.chats
    ]
    await message.answer("\n\n".join(local_settings))
