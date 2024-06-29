from aiogram.fsm.state import StatesGroup, State


class SignUp(StatesGroup):
    name = State()
    phone = State()
    location = State()
    position = State()
    salary = State()
