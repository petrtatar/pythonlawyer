from aiogram import Router
from aiogram.types import Message
import keyboards.keyboards as kb


router = Router()

@router.message()
async def other_messages(messeage:Message):
    await messeage.answer(
        f"Can't understand it. Do you want to play with me?",
        reply_markup=kb.play
    )
