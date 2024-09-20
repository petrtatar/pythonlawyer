import asyncio
import logging

from aiogram import Bot, Dispatcher
import os

from aiogram.types import BotCommand, BotCommandScopeDefault
from dotenv import load_dotenv
from handlers import other_handlers, user_handlers

load_dotenv()


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='To launch the bot',
        ),
        BotCommand(
            command='help',
            description='Information about the bot'
        )
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())


def register_handlers(dp: Dispatcher):
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)


async def run():
    bot_token = os.getenv('BOT_TOKEN')
    bot = Bot(bot_token)
    dp = Dispatcher()

    await set_commands(bot)
    register_handlers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(run())
