from aiogram import Dispatcher
from aiogram.types import Message
from contextlib import suppress


async def check_message(m: Message):
    with suppress(IndexError):
        if m.text[-1] == '.' and m.text[-2] != '.' and m.forward_from_chat is None:
            await m.delete()


def register_user(dp: Dispatcher):
    dp.register_message_handler(check_message, chat_type=["group", "supergroup"])
