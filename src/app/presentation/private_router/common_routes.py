from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
import inspect

router = Router(name="privat common router")

@router.message(CommandStart())
async def start(message: Message):
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
            /unsetme -  убирает глобальный эмодзи.

            В личных сообщениях вы можете выбрать глобальный параметр регистации, \
            однако локальные параметры регистрации имеют больший приоритет. 
            Аналогичная ситуация с emoji. 
           """
    await message.answer(inspect.cleandoc(text))

@router.message(Command("reg"))
async def reg(message: Message):
    pass