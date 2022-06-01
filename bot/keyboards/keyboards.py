from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton


def first_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    btn_work = InlineKeyboardButton(text='Работаю', callback_data='work')
    btn_rest = InlineKeyboardButton(text='Отдыхаю', callback_data='rest')
    kb.add(btn_work).add(btn_rest)
    return kb.as_markup()


def work_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    btn_office = InlineKeyboardButton(text='В офисе', callback_data='office')
    btn_remote = InlineKeyboardButton(text='На удаленке', callback_data='remote')
    btn_back = InlineKeyboardButton(text='Назад', callback_data='back')
    kb.row(btn_office, btn_remote).row(btn_back)
    return kb.as_markup()


def rest_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    btn_back = InlineKeyboardButton(text='Назад', callback_data='back')
    btn_rest_confirm = InlineKeyboardButton(text='Подтвердить', callback_data='rest_confirm')
    kb.add(btn_rest_confirm, btn_back)
    return kb.as_markup()
