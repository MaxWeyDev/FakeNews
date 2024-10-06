# Импорт из библиотеки aiogram
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
import is_it_fake
import os

router = Router()


# Обработчик кнопки старт
@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(
        "Привет! Отправь мне новость, и я скажу тебе, фейк это или нет. /nЧтобы получить больше информации, используй команду /help")


@router.message(Command("help"))
async def help_command(msg: Message):
    await msg.answer(
        "Отправь текст новости боту, и он постарается ответить, фейк это или нет. Бот не будет обсуждать опасные темы, связанные в войной, политикой и т.п. Пока что ИИ не всегда способен точно определять фейки, но он старается :) .")


@router.message()
async def is_it_fake_answer(message: types.message):
    result = await is_it_fake.check_text_for_fake(
        os.getenv('API_KEY'),
        os.getenv('FOLDER_ID'),
        user_text=message.text)
    await message.answer(result)
