# Импорт из библиотеки aiogram
import asyncio

from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
import is_it_fake
import os

router = Router()


# Обработчик кнопки старт
@router.message(Command("start"))
async def start_handler(msg: Message):
    users_list = open("users.txt", "r")
    users_ids = set(users_list.readlines())
    if msg.from_user.id not in users_ids:
        with open("users.txt", 'a') as f:
            #print(msg.from_user.id)
            print(msg.from_user.id, file=f)
    await msg.answer(
        "Привет! Отправь мне новость, и я скажу тебе, фейк это или нет. Чтобы получить больше информации, используй команду /help")


@router.message(Command("help"))
async def help_command(msg: Message):
    await msg.answer(
        "Отправь текст новости боту, и он постарается ответить, фейк это или нет. Бот не будет обсуждать опасные темы, связанные в войной, политикой и т.п. Пока что ИИ не всегда способен точно определять фейки, но он старается :) .")


@router.message()
async def is_it_fake_answer(message: types.message):
    have_sense = await is_it_fake.check_text_for_sense(
        os.getenv('API_KEY'),
        os.getenv('FOLDER_ID'),
        user_text=message.text,
    )
    if not have_sense:
        await message.answer('Ваше сообщение не имеет смысла')
        return
    await asyncio.sleep(1)
    result = await is_it_fake.check_text_for_fake(
        os.getenv('API_KEY'),
        os.getenv('FOLDER_ID'),
        user_text=message.text,
    )
    print(result)
    await message.answer(result)
