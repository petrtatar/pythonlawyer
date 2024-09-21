from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start_game_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Start game', callback_data='start_game')]
])


play_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Rock🪨', callback_data='rock')],
    [InlineKeyboardButton(text='Paper📄', callback_data='paper')],
    [InlineKeyboardButton(text='Scissors✂️', callback_data='scissors')],
])
