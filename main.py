# используем библиотеку aiogram, т.к. она позволяет создавать асинхронных ботов в Телеграме
import asyncio
import logging
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import router



# токен нашего бота от BotFather
BOT_TOKEN = "7402051024:AAFhS1emEY1NMv0MxZAw3RusYi1ZdtTJ-ck"



async def main():

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())



# Работает пока не выключим
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())