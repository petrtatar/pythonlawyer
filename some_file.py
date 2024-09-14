import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

BOT_TOKEN = '7321879151:AAHgnM9nWtnMF41uGp8GS5hEeiaMRVYbYuM'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

ATTEMPTS = 5


user = {'in_game': False,
        'secret_number': None,
        'attempts': None,
        'total_games': 0,
        'wins': 0
}


def get_random_number() -> int:
    return random.randint(a=1, b=100)


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text='Угадай число')


@dp.message(Command(commands='help'))
async def cmd_help(message: Message):
    await message.answer(text=
                         'Это бот для игры в угадай число.\n\n'
                         'Я загадываю число от 1 до 100 и его нужно угадать за 5 попыток.')


@dp.message(Command(commands='stat'))
async def cmd_stat(message: Message):
    await message.answer(text=
        f'Всего игр сыграно: {user['total_games']}\n'
        f'Игр выиграно: {user['wins']}'
    )


@dp.message(Command(commands='cancel'))
async def cmd_cancel(message: Message):
    if user['in_game']:
        user['in_game'] = False
        await message.answer(
            text=f'Вы вышли из игры. Если захотите еще раз сыграть, напишите об этом'
        )
    else:
        await message.answer(
            f'А мы так с вами и не играем'
            f'Может сыграем разок?'
        )


@dp.message(F.text.lower().in_(['да', 'давай', 'хочу', 'сыграем', 'играть']))
async def positive_answer(message: Message):
    if not user['in_game']:
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = ATTEMPTS
        await message.answer(
            f'Я загадал число от 1 до 100. '
            f'Попробуй угадать его.'
        )
    else:
        await message.answer(
            f'Пока мы играем в игру, я могу реагировать только на числа от 1 до 100'
            f'и команды /start, /cancel, /stat'
        )


@dp.message(F.text.lower().in_(['нет', 'не хочу', 'не буду']))
async def negative_question(message: Message):
    if not user['in_game']:
        await message.answer(
            f'Хорошо. Если захотите играть, просто напишите об этом.'
        )
    else:
        await message.answer(
            f'Игра уже идет. Введите число от 1 до 100'
        )


@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def guessing_attempt(message: Message):
    if user['in_game']:
        if int(message.text) == user['secret_number']:
            user['in_game'] = False
            user['total_games'] += 1
            user['wins'] += 1
            await message.answer(
                f'Поздравляю! Вы победили!\n'
                f'Сыграем еще?'
            )
        elif int(message.text) > user['secret_number']:
            user['attempts'] -= 1
            await message.answer(
                f'Мое число меньше. Попробуй еще раз'
            )
        elif int(message.text) < user['secret_number']:
            user['attempts'] -= 1
            await message.answer(
                f'Мое число больше. Попробуй еще раз'
            )

        if user['attempts'] == 0:
            user['in_game'] = False
            user['total_games'] += 1
            await message.answer(
                f'К сожалению, вы проиграли. Мое число было'
                f'{user['secret_number']}.'
                f'\n\n Попробуем еще раз?'
            )
    else:
        await message.answer(
            f'Мы еще не играем. Начать игру?'
        )


@dp.message()
async def other_messages(message: Message):
    await message.answer(
        f'Я еще не настолько универсальный бот. Давайте лучше сыграем в игру?'
    )


if __name__ == '__main__':
    dp.run_polling(bot)