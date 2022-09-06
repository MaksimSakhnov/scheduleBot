from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text, state
from loader import dp
from keyboards.default import facultets_kb, getSchedule_kb
from states import register
from parsing import getVar, getUrl
import datetime
from parsing import getSchedule
from utils.db_api import quick_commands as commands


@dp.message_handler(Command('start'))
async def command_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}, выбери свой факультет ниже',
                         reply_markup=facultets_kb)
    await register.waiting_for_fac_name.set()


@dp.message_handler(state=register.waiting_for_fac_name)
async def state_waiting_for_fac_name(message: types.Message, state: FSMContext):
    answer = message.text
    print(answer)
    var = getVar(answer)
    print(var)
    if var == -1:
        await message.answer("Такого факультета нет, введи еще раз")
        await register.waiting_for_fac_name.set()
    else:
        await state.update_data(waiting_for_fac_name=var)
        await message.answer("Введи номер группы", reply_markup=types.ReplyKeyboardRemove())
        await register.waiting_for_group_number.set()


@dp.message_handler(state=register.waiting_for_group_number)
async def state_waiting_for_group_number(message: types.Message, state: FSMContext):
    data = await state.get_data()
    var = data.get('waiting_for_fac_name')
    answer = message.text
    url = getUrl(var, answer)
    if url == -1:
        await message.answer("Такой группы нет, введи еще раз")
        await register.waiting_for_group_number.set()
    else:
        try:
            user = await commands.select_user(user_id=message.from_user.id)
            if (user.user_id == message.from_user.id):
                await commands.update_url(message.from_user.id, url)
        except Exception:
            await commands.add_user(user_id=message.from_user.id, user_url=url)
        await state.update_data(waiting_for_group_number=url)
        await state.finish()
        await message.answer("Чтобы получить расписание, нажимай на кнопки ниже)", reply_markup=getSchedule_kb)


@dp.message_handler(lambda message: message.text == "Сегодня")
async def getSchedule_today(message: types.Message):
    id = message.from_user.id
    print(id)
    user = await commands.select_user(id)
    url = user.user_url
    print(user)
    weekday = datetime.datetime.today().isoweekday()
    schedule = getSchedule(weekday, url)
    await message.answer(schedule)
    # if action == 'tomorrow':
    #
    # if action == 'week':


@dp.message_handler(lambda message: message.text == "Завтра")
async def getSchedule_today(message: types.Message):
    id = message.from_user.id
    print(id)
    user = await commands.select_user(id)
    url = user.user_url
    print(user)
    weekday = datetime.datetime.today().isoweekday() + 1
    if (weekday == 8):
        weekday = 1
    schedule = getSchedule(weekday, url)
    await message.answer(schedule)

@dp.message_handler(lambda message: message.text == "На неделю")
async def getSchedule_today(message: types.Message):
    id = message.from_user.id
    print(id)
    user = await commands.select_user(id)
    url = user.user_url
    print(user)
    for i in range(1, 8):
        schedule = getSchedule(i, url)
        await message.answer(schedule)