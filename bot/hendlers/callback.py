from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hlink

from bot.db import DB
from bot.db.database import UserState
from bot.keyboards.keyboards import rest_kb, work_kb, first_kb

router = Router()


async def cb_work(call: CallbackQuery):
    await call.message.edit_text(text='И где ты сегодня работаешь?', reply_markup=work_kb())


async def cb_rest(call: CallbackQuery):
    link = hlink('Лене', 'https://t.me/ENTyumentseva')
    await call.message.edit_text(text=f'Тогда пиши {link}, по какому поводу', reply_markup=rest_kb(),
                                 disable_web_page_preview=True)


async def cb_back(call: CallbackQuery):
    await call.message.edit_text(text='Хегей, пора отмечаться!\n Чем сегодня занимаешься', reply_markup=first_kb())


async def cb_office(call: CallbackQuery):
    DB.set_state(user_id=call.from_user.id, state=UserState.OFFICE, value=True)
    await call.message.edit_text(text='Отлично, тебя отметили!\nВ офисе')


async def cb_remote(call: CallbackQuery):
    DB.set_state(user_id=call.from_user.id, state=UserState.REMOTE, value=True)
    await call.message.edit_text(text='Отлично, тебя отметили!\nУдаленно')


async def cb_rest_confirm(call: CallbackQuery):
    DB.set_state(user_id=call.from_user.id, state=UserState.REST, value=True)
    await call.message.edit_text(text='Отлично, тебя отметили!\nОтдыхаешь')


@router.callback_query()
async def all_callback(call: CallbackQuery):
    match call.data:
        case 'work':
            await cb_work(call)
        case 'rest':
            await cb_rest(call)
        case 'back':
            await cb_back(call)
        case 'office':
            await cb_office(call)
        case 'remote':
            await cb_remote(call)
        case 'rest_confirm':
            await cb_rest_confirm(call)


