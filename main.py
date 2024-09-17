from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, Message

BOT_TOKEN = '7321879151:AAHgnM9nWtnMF41uGp8GS5hEeiaMRVYbYuM'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


button_1 = KeyboardButton(text='Собак 🐕')
button_2 = KeyboardButton(text='Огурцов 🥒')

keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]])


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        text=f'Чего кошки боятся больше?',
        reply_markup=keyboard
    )


@dp.message(F.text == 'Собак 🐕')
async def dog_answer(message: Message):
    await message.answer(
        text=f'Да, собак. Но вы видели, как они боятся огурцов?',
        reply_markup=ReplyKeyboardRemove()
    )


@dp.message(F.text == 'Огурцов 🥒')
async def cucumber_answer(message: Message):
    await message.answer(
        text=f'Да, иногда кажется, что они действительно больше боятся огурцов.',
        reply_markup=ReplyKeyboardRemove()
    )


if __name__ == '__main__':
    dp.run_polling(bot)
