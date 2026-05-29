from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
import inspect
from dishka import FromDishka
from src.app.application.interactors.private import (
    StartInteractor,
    RegisterUserGlobalyInteractor,
)

router = Router(name="privat common router")


@router.message(CommandStart(), F.chat.type == "private")
async def start(message: Message, interactor: FromDishka[StartInteractor]):
    user = message.from_user
    if user is None:
        await message.answer("Вы не можете писать от лица канала.")
        return
    await interactor(user.id)
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


@router.message(Command("reg"))
async def reg(message: Message, interactor: FromDishka[RegisterUserGlobalyInteractor]):
    user = message.from_user
    if user is None:
        await message.answer("Вы не можете писать от лица канала.")
        return
    await interactor(user.id)
    await message.answer("Вы установили глобальную регистрацию.")
