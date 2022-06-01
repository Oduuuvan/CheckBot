import asyncio

import aioschedule
from aiogram import Bot

from bot.db import DB
from bot.keyboards.keyboards import first_kb


async def first_mailing(bot: Bot):
    for user_id in DB.get_all_user_id():
        await bot.send_message(user_id[0], text='Хегей, пора отмечаться!\n Чем сегодня занимаешься',
                               reply_markup=first_kb())


async def second_mailing(bot: Bot):
    await bot.send_message(423193720, text='Рассылка 2')


async def set_all_satate_false():
    DB.set_all_false()


async def mailing_schedule(bot: Bot):
    aioschedule.every().day.at('21:43').do(first_mailing, bot)
    aioschedule.every().day.at('21:44').do(second_mailing, bot)
    aioschedule.every().day.at('21:46').do(set_all_satate_false)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(5)
