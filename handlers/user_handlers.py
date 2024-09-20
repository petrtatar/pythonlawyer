from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards import keyboards as kb
import random

router = Router()


game_list = ['Rock🪨', 'Paper📄', 'Scissors✂️']


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f'A bot for the play "Rock-paper-scissors".',
        reply_markup=kb.start_game
    )


@router.message(Command(commands='help'))
async def cmd_help(message: Message):
    await message.answer(
        f'If you want to start the game, please, press the button "Start game"',
        reply_markup=kb.start_game
    )


@router.message(F.text == 'Start game')
async def the_game(message: Message):
    await message.answer(
        f'Choose your item.',
        reply_markup=kb.play
    )


@router.message(F.text == 'Rock🪨')
async def play_rock(message: Message):
    bot_choice = random.choice(game_list)
    if bot_choice == 'Rock🪨':
        await message.answer(
            f"{bot_choice}\n\nDRAW! Let's do it again!",
            reply_markup=kb.play
        )
    if bot_choice == 'Paper📄':
        await message.answer(
            f"{bot_choice}\n\nYes, I won! Don't get upset, we can play one more time!",
            reply_markup=kb.play
        )
    if bot_choice == 'Scissors✂️':
        await message.answer(
            f"{bot_choice}\n\nOkey, you beat me. But I'll win next time!",
            reply_markup=kb.play
        )


@router.message(F.text == 'Paper📄')
async def play_rock(message: Message):
    bot_choice = random.choice(game_list)
    if bot_choice == 'Paper📄':
        await message.answer(
            f"{bot_choice}\n\nDRAW! Let's do it again!",
            reply_markup=kb.play
        )
    if bot_choice == 'Scissors✂️':
        await message.answer(
            f"{bot_choice}\n\nYes, I won! Don't get upset, we can play one more time!",
            reply_markup=kb.play
        )
    if bot_choice == 'Rock🪨':
        await message.answer(
            f"{bot_choice}\n\nOkey, you beat me. But I'll win next time!",
            reply_markup=kb.play
        )


@router.message(F.text == 'Scissors✂️')
async def play_rock(message: Message):
    bot_choice = random.choice(game_list)
    if bot_choice == 'Scissors✂️':
        await message.answer(
            f"{bot_choice}\n\nDRAW! Let's do it again!",
            reply_markup=kb.play
        )
    if bot_choice == 'Rock🪨':
        await message.answer(
            f"{bot_choice}\n\nYes, I won! Don't get upset, we can play one more time!",
            reply_markup=kb.play
        )
    if bot_choice == 'Paper📄':
        await message.answer(
            f"{bot_choice}\n\nOkay, you beat me. But I'll win next time!",
            reply_markup=kb.play
        )
