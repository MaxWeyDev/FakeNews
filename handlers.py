# Импорт из библиотеки aiogram
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command



router = Router()



# Обработчик кнопки старт
@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет!")

# Очевидно нужны ещё обработчики, как минимум один для новости с возвратом ложь это или нет, но после запроса уже сделаю.
# Плюс надо поменять текст приветственного сообщения, добавить информации. Потом.



