from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

getSchedule_kb = ReplyKeyboardMarkup(resize_keyboard=True) \
    .row(KeyboardButton(text='Сегодня', callback_data='get_today'),
         KeyboardButton(text="Завтра", callback_data='get_tomorrow'),
         KeyboardButton(text="На неделю", callback_data='get_week'))
    #.add(KeyboardButton("Чис/Знам ?"), callback_data='get_type')
