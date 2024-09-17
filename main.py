from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

BOT_TOKEN = '7321879151:AAHgnM9nWtnMF41uGp8GS5hEeiaMRVYbYuM'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
kb_builder = ReplyKeyboardBuilder()


buttons: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i + 1}') for i in range(10)
]


kb_builder.row(*buttons, width=4)


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        text=f'Чего кошки боятся больше?',
        reply_markup=kb_builder.as_markup(resize_keyboard=True)
    )


@dp.message(F.text == 'Собак 🐕')
async def dog_answer(message: Message):
    await message.answer(
        text=f'Да, собак. Но вы видели, как они боятся огурцов?'
    )


@dp.message(F.text == 'Огурцов 🥒')
async def cucumber_answer(message: Message):
    await message.answer(
        text=f'Да, иногда кажется, что они действительно больше боятся огурцов.'
    )


if __name__ == '__main__':
    dp.run_polling(bot)
