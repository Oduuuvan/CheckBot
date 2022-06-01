from aiogram import Router
from aiogram.types import Message

from bot.db import DB
from bot.keyboards.keyboards import first_kb

router = Router()


@router.message(commands=['start'])
async def cmd_satrt(message: Message) -> None:
    if not DB.user_exists(message.from_user.id):
        DB.add_user(message.from_user.id, message.from_user.username,
                    message.from_user.first_name, message.from_user.last_name)
        await message.answer('Привет, я тебя запомнил!')
    else:
        await message.answer('Я тебя помню!')


@router.message(commands=['stop'])
async def cmd_stop(message: Message) -> None:
    if DB.user_exists(message.from_user.id):
        DB.remove_user(message.from_user.id)
        await message.answer('До встречи!\nЕсли снова захочешь получать уведомления напиши /start')
    else:
        await message.answer('Я тебя не знаю -_-')


@router.message(commands=['test'])
async def cmd_test(message: Message) -> None:
    await message.answer(text='test', reply_markup=first_kb())
