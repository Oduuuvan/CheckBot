import asyncio
import logging
from aiogram import Dispatcher, Bot

from bot.commands import set_commands
from bot.config import BOT_TOKEN
from bot.hendlers import default_commands, callback


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    # Creating bot and its dispatcher
    bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    # Connecting routers
    dp.include_router(default_commands.router)
    dp.include_router(callback.router)

    await set_commands(bot)
    print('Bot started')
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
