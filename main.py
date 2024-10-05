from aiogram import Bot, Dispatcher, executor, types
TOKEN = '7402051024:AAFhS1emEY1NMv0MxZAw3RusYi1ZdtTJ-ck'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start']) #Явно указываем в декораторе, на какую команду реагируем.
async def send_welcome(message: types.Message):
   await message.reply("Привет!") #Так как код работает асинхронно, то обязательно пишем await.
@dp.message_handler()
async def echo(message: types.Message): #Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.
   await message.answer(message.text)
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
