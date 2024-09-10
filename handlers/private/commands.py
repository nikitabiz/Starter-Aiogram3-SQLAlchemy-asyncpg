from aiogram.types import Message
from aiogram.filters import CommandStart

from loader import dp


@dp.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer("<b>✌️ Привет!</b>")