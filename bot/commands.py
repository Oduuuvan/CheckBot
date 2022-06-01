from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot):
    commands_list = [
                    BotCommand(command='start', description='Вас добавят в базу данных для будущих уведомлений'),
                    BotCommand(command='stop', description='Вас удалят из базы данных и больше не будут присылать \
                                                             уведомления'),
                    BotCommand(command='test', description='Отладочная команда')
                    ]
    await bot.set_my_commands(commands=commands_list)
