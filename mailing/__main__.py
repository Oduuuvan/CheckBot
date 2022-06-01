import asyncio

from aiogram import Bot

from mailing.schedules import mailing_schedule
from bot.config import BOT_TOKEN


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
    await mailing_schedule(bot)


if __name__ == '__main__':
    asyncio.run(main())
