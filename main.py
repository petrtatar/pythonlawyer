import asyncio
import logging

import aiogram
from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
from handlers import other_handlers, user

load_dotenv()

bot_token = os.getenv('BOT_TOKEN')
bot = Bot(bot_token)

dp = Dispatcher()

dp.include_router(user.router)
dp.include_router(other_handlers.router)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        dp.run_polling(bot)
    except KeyboardInterrupt:
        print('Exit')
