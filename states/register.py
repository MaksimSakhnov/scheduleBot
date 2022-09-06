from aiogram.dispatcher.filters.state import StatesGroup, State


class register(StatesGroup):
    waiting_for_fac_name = State()
    waiting_for_group_number = State()
    waiting_for_get_schedule = State()
