from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from keyboards import keyboards as kb
import random

router = Router()


game_list = ['Rock🪨', 'Paper📄', 'Scissors✂️']


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f'A bot for the play "Rock-paper-scissors".',
        reply_markup=kb.start_game_inline
    )


@router.message(Command(commands='help'))
async def cmd_help(message: Message):
    await message.answer(
        f'If you want to start the game, please, press the button "Start game"',
        reply_markup=kb.start_game_inline
    )


@router.callback_query(F.data == 'start_game')
async def the_game(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(
        f'Choose your item.',
        reply_markup=kb.play_inline
    )


@router.callback_query(F.data == 'rock')
async def play_rock(callback: CallbackQuery):
    bot_choice = random.choice(game_list)
    if bot_choice == 'Rock🪨':
        await callback.answer('')
        await callback.message.edit_text(
            f"{bot_choice}\n\nDRAW! Let's do it again!",
            reply_markup=kb.play_inline
        )
    if bot_choice == 'Paper📄':
        await callback.answer('')
        await callback.message.edit_text(
            f"{bot_choice}\n\nYes, I won! Don't get upset, we can play one more time!",
            reply_markup=kb.play_inline
        )
    if bot_choice == 'Scissors✂️':
        await callback.answer('')
        await callback.message.edit_text(
            f"{bot_choice}\n\nOkey, you beat me. But I'll win next time!",
            reply_markup=kb.play_inline
        )


@router.callback_query(F.data == 'paper')
async def play_rock(callback: CallbackQuery):
    bot_choice = random.choice(game_list)
    if bot_choice == 'Paper📄':
        await callback.answer('')
        await callback.message.edit_text(
            f"{bot_choice}\n\nDRAW! Let's do it again!",
            reply_markup=kb.play_inline
        )
    if bot_choice == 'Scissors✂️':
        await callback.answer('')
        await callback.message.edit_text(
            f"{bot_choice}\n\nYes, I won! Don't get upset, we can play one more time!",
            reply_markup=kb.play_inline
        )
    if bot_choice == 'Rock🪨':
        await callback.answer('')
        await callback.message.edit_text(
            f"{bot_choice}\n\nOkey, you beat me. But I'll win next time!",
            reply_markup=kb.play_inline
        )


@router.callback_query(F.data == 'scissors')
async def play_rock(callback: CallbackQuery):
    bot_choice = random.choice(game_list)
    if bot_choice == 'Scissors✂️':
        await callback.answer('')
        await callback.message.edit_text(
            f"{bot_choice}\n\nDRAW! Let's do it again!",
            reply_markup=kb.play_inline
        )
    if bot_choice == 'Rock🪨':
        await callback.answer('')
        await callback.message.edit_text(
            f"{bot_choice}\n\nYes, I won! Don't get upset, we can play one more time!",
            reply_markup=kb.play_inline
        )
    if bot_choice == 'Paper📄':
        await callback.answer('')
        await callback.message.edit_text(
            f"{bot_choice}\n\nOkay, you beat me. But I'll win next time!",
            reply_markup=kb.play_inline
        )
