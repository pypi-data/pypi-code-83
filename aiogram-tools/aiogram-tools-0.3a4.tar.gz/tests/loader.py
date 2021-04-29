import asyncio

from aiogram import Dispatcher

import config
from aiogram_tools._bot import Bot

bot = Bot(
    token=config.BOT_TOKEN,
    bound_userbot_api_id=config.USERBOT_API_ID,
    bound_userbot_api_hash=config.USERBOT_API_HASH,
)

dp = Dispatcher(bot)

loop = asyncio.get_event_loop()
coro = bot.create_group(title='test4', users=['LDmitriy1998'])
loop.run_until_complete(coro)
