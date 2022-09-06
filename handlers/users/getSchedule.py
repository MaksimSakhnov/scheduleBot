from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text, state
from loader import dp
import datetime
from parsing import getSchedule
from states import register


@dp.callback_query_handler(Text(startswith="get_"), state=register)
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split("_")[1]
    print(action)
    data = await state.get_data()
    url = data.get('waiting_for_group_number')
    print(url)
    if action == 'today':
        weekday = datetime.datetime.today().isoweekday()
        schedule = getSchedule(weekday, url)
        await call.message.answer(schedule)
    if action == 'tomorrow':
        weekday = datetime.datetime.today().isoweekday() + 1
        if (weekday == 8):
            weekday = 1
        schedule = getSchedule(weekday, url)
        await call.message.answer(schedule)
    if action == 'week':
        for i in range(1, 8):
            schedule = getSchedule(weekday, url)
            await call.message.answer(schedule)
