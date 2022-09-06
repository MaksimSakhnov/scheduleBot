from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from aiogram import executor
from handlers import dp
from loader import db
from utils.db_api.db_gino import on_startUp

async def on_startup(dp):
    await on_startUp(dp)
    await on_startup_notify(dp)
    await set_default_commands(dp)
    print("Бот запущен")

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)