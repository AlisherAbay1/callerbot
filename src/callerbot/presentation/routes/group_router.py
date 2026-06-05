from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, JOIN_TRANSITION
from aiogram.types import Message, ChatMemberUpdated
import inspect
from dishka import FromDishka
from callerbot.application.interactors.group import (
    RegisterUserLocallyInteractor,
    JoinChatInteractor,
    UnRegisterUserLocallyInteractor,
    SetEmojiLocallyInteractor,
)
from callerbot.presentation.middlware import GroupMiddleware
from emoji import is_emoji, emoji_count

router = Router(name="group common router")
router.my_chat_member.filter(F.chat.type.in_(("group", "supergroup")) & F.from_user)
router.message.filter(F.chat.type.in_(("group", "supergroup")) & F.from_user)
router.message.outer_middleware(GroupMiddleware())


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))
async def on_chat_joining(
    event: ChatMemberUpdated, interactor: FromDishka[JoinChatInteractor]
):
    assert event.chat
    assert event.chat.title
    await interactor(chat_tg_id=event.chat.id, chat_title=event.chat.title)
    text = """
            Вы добавили меня в группу. 
            Список команд для чата:
            /all - тегает всех юзеров, которые дали на это согласие. 
            /reg - регистрирует вас в список вызываемых юзеров. 
            /unreg - убирает вас в список вызываемых юзеров.
            /setme (emoji) - устанавливает эмодзи. 
            /unsetme (emoji) - убирает эмодзи. 
           """
    await event.answer(inspect.cleandoc(text))


@router.message(Command("reg"))
async def reg_locally(
    message: Message, interactor: FromDishka[RegisterUserLocallyInteractor]
):
    assert message.from_user
    await interactor(user_tg_id=message.from_user.id)
    await message.answer("Вы установили локальную регистрацию.")


@router.message(Command("unreg"))
async def unreg_locally(
    message: Message, interactor: FromDishka[UnRegisterUserLocallyInteractor]
):
    assert message.from_user
    await interactor(user_tg_id=message.from_user.id)
    await message.answer("Вы убрали локальную регистрацию.")


@router.message(Command("setme"))
async def setme_locally(
    message: Message,
    command: CommandObject,
    interactor: FromDishka[SetEmojiLocallyInteractor],
):
    assert message.from_user
    emoji = command.args
    if emoji is None:
        await message.answer("Вы должны передать смайлик.")
        return
    if not (is_emoji(emoji) and emoji_count(emoji) == 1):
        await message.answer("Передайте эмодзи.")
        return
    await interactor(tg_id=message.from_user.id, emoji=emoji)
    await message.answer(f"Вы установили локальный эмодзи: {emoji}")
