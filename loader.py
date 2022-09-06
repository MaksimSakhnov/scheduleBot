from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

from utils.db_api.db_gino import db

# Объект бота
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

# Диспетчер для бота
dp = Dispatcher(bot, storage=MemoryStorage())

__all__=['bot', 'storage','dp','db']
