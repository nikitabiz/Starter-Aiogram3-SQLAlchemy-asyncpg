import asyncio
import handlers

from loader import dp, bot
from aiogram.types import BotCommandScopeAllPrivateChats
from settings.commands import private_commands
from database.queries import create_tables
from utils.tasks import *


async def start():   
    await create_tables()
    await bot.set_my_commands(
        private_commands, 
        scope=BotCommandScopeAllPrivateChats()
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try: 
        loop = asyncio.get_event_loop()
        loop.run_until_complete(start()) 
    except KeyboardInterrupt: 
        pass
