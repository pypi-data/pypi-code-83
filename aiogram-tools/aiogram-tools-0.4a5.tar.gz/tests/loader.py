import asyncio

import config
from aiogram_tools import Dispatcher
from aiogram_tools._bot import Bot

bot = Bot(
    token=config.BOT_TOKEN,
    bound_userbot_api_id=config.USERBOT_API_ID,
    bound_userbot_api_hash=config.USERBOT_API_HASH,
)

dp = Dispatcher(bot)

loop = asyncio.get_event_loop()
