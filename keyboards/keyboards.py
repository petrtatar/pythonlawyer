from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_game = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Start game')]
])


play = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Rock🪨'), KeyboardButton(text='Paper📄'), KeyboardButton(text='Scissors✂️')]
])
