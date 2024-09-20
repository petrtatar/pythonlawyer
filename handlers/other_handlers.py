from aiogram import Router, Bot
from aiogram.types import Message
import keyboards.keyboards as kb

router = Router()


@router.message()
async def other_messages(message: Message):
    await message.answer(
        f"Can't understand it. Do you want to play with me?",
        reply_markup=kb.play
    )
