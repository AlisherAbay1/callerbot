from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
import inspect
from dishka import FromDishka
from src.app.application.interactors.private import (
    StartInteractor,
    RegisterUserGlobalyInteractor,
    UnRegisterUserGlobalyInteractor,
)

router = Router(name="privat common router")


@router.message(CommandStart(), F.chat.type == "private" & F.from_user)
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
            
            Список команд для личных сообщений:
            /reg - вы будете зарегистрированы во всех чатах по дефолту. 
            /unreg - вас уберут из регистрации во всех чатах по дефолту. 
            /setme (emoji) - устанавливает глобальный эмодзи.
            /unsetme - убирает глобальный эмодзи.
            /showsettings - вы увидите свои настройки. Глобальные и локальные. 

            В личных сообщениях вы можете выбрать глобальный параметр регистации, 
            однако локальные параметры регистрации имеют больший приоритет. 
            Аналогичная ситуация с emoji. 
           """
    await message.answer(inspect.cleandoc(text))


@router.message(Command("reg"), F.from_user)
async def reg(message: Message, interactor: FromDishka[RegisterUserGlobalyInteractor]):
    assert message.from_user
    await interactor(message.from_user.id)
    await message.answer("Вы установили глобальную регистрацию.")


@router.message(Command("reg"), F.from_user)
async def unreg(
    message: Message, interactor: FromDishka[UnRegisterUserGlobalyInteractor]
):
    assert message.from_user
    await interactor(message.from_user.id)
    await message.answer("Вы убрали глобальную регистрацию.")
