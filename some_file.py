from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

BOT_TOKEN = '7321879151:AAHgnM9nWtnMF41uGp8GS5hEeiaMRVYbYuM'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(text='Эхо-бот')


@dp.message(Command(commands=['help']))
async def cmd_help(message: Message):
    await message.reply('Напиши мне сообщение и я его повторю')


@dp.message(F.photo)
async def send_echo_photo(message: Message):
    await message.answer_photo(message.photo[-1].file_id)


@dp.message()
async def send_echo_message(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)