from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ContentType

BOT_TOKEN = '7321879151:AAHgnM9nWtnMF41uGp8GS5hEeiaMRVYbYuM'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def cmd_start(message: Message):
    await message.reply(text='Эхо-бот')


async def cmd_help(message: Message):
    await message.reply('Напиши мне сообщение и я его повторю')


async def send_echo_message(message: Message):
    await message.reply(text=message.text)

dp.message.register(cmd_start, CommandStart())
dp.message.register(cmd_help, Command(commands=['help']))
dp.message.register(send_echo_message)


if __name__ == '__main__':
    dp.run_polling(bot)