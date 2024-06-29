import time
from pprint import pprint
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType
from states import SignUp
from random import randint, seed

yorn = ""
reg = True
vacancy_id_status = False


async def info(message: Message, bot: Bot, state: FSMContext):
    profile = await bot.get_chat(chat_id=message.from_user.id)
    user = message.from_user
    data = f"""Your id is "{message.from_user.id}"\n Your first name is "{user.first_name}"\n"""
    if user.last_name:
        data += f"""Your last name is "{user.last_name}"\n"""
    if user.username:
        data += f"Your username is @{user.username}\n"
    if profile.bio:
        data += f"""Your bio is "{profile.bio}"""

    await message.answer(text=data)
    # await bot.send_message(chat_id="1282767793", text=data)
    pprint(data)


async def bot_start(message: Message):
    await message.answer(text=f"Assalomu alaykum xurmatli {message.from_user.first_name}, BOTga xush kelibsiz to'liq ma'lumot olish uchun:  /help")


async def start(bot: Bot):
    await bot.send_message(chat_id="1282767793", text="Bot muvaffaqiyatli ishga tushdi ✅")


async def stop(bot: Bot):
    await bot.send_message(chat_id="1282767793", text="Bot to'xtatildi ❌")


async def help(message: Message):
    await message.answer(text="""
/start -> Botni boshlash
/help -> Yordam
/info -> O'zingiz haqingizda ma'lumot olish
/vacancy -> E'lon berish
""")


async def vacancy(message: Message,state: FSMContext):
    global yorn, for_yorn, vacancy_id_status, reg
    vacancy_id_status = False
    reg = True
    for_yorn = 1
    yorn = ""
    await message.answer("🙆‍♂️Ismingizni kiriting: ")
    await state.set_state(SignUp.name)


async def register_name(message: Message,state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("☎️Telefon raqamingizni kiriting: +998XXXXXXXXX ")
    await state.set_state(SignUp.phone)


async def register_phone(message: Message,state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("📍Addresni kiriting: ")
    await state.set_state(SignUp.location)


async def register_location(message: Message,state: FSMContext):
    await state.update_data(location=message.text)
    await message.answer("👨‍💻Lavozimni kiriting: ")
    await state.set_state(SignUp.position)


async def register_position(message: Message,state: FSMContext):
    global vacancy_id_status
    await state.update_data(position=message.text)
    await message.answer("💸Maoshni kiriting: ")
    await state.set_state(SignUp.salary)
    vacancy_id_status = False


async def register_finish(message: Message,bot: Bot, state: FSMContext):
    global yorn, reg, vacancy_id, vacancy_id_status

    await state.update_data(salary=message.text)
    data = state.get_data()
    data = await data
    with open("IDs.txt", "r") as f:
        file = f.read()
        seed(time.time())
        while not vacancy_id_status:
            vacancy_id = randint(100000000, 999999999)
            used_IDs = file.split(" ")
            if not str(vacancy_id) in str(used_IDs):
                vacancy_id_status = True



    txt = f"""💾E'lon idsi: {vacancy_id}

🙆‍♂️Ism: {data.get("name")}
☎️Ma'lumot uchun: {data.get("phone")}
📍Manzil: {data.get("location")}
👨‍💻Lavozim: {data.get("position")}
💸Moash: {data.get("salary")}
    """
    if reg:
        await bot.send_message(chat_id=message.from_user.id, text="👀E'lon ko'rinishi👇")
        await message.answer(text=txt)
        await bot.send_message(chat_id=message.from_user.id, text="Barcha ma'lumotlar to'grimi? Yes/No")
        reg = False
    yorn = message.text
    if yorn == "Yes":
        with open("IDs.txt", "a") as f:
            f.write(f" {vacancy_id}")
        await bot.send_message(chat_id="1282767793", text=txt)
        await bot.send_message(chat_id=message.from_user.id,
            text=f"""Uzcard:
0000000000000000
X x
20.000 so'm
""")
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"""To'lovni qilgach chekni adminga(@jez0w) e'lon idsi bilan birgalikda 
yuboring va admin javobini kuting.""")
    elif yorn == "No":
        await bot.send_message(chat_id=message.from_user.id,
                               text="/vacancy buyrug'i orqali boshidan boshlashingiz mumkin.")
        reg = True








