import os
import asyncio
import logging
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import router
from dotenv import load_dotenv
import is_it_fake



async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('BOT_TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())



# Работает пока не выключим
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())