from asyncio import *
from os import getenv
from aiogram import *
from aiogram.filters import Command
from aiogram.types import Message, BotCommand
from dotenv import load_dotenv

from functions import *

load_dotenv()

TOKEN = getenv('BOT_TOKEN')

dp = Dispatcher()


async def main(dp):
    bot = Bot(token=TOKEN)
    await bot.set_my_commands(
        [
            BotCommand(command="/start", description="Start the bot"),
            BotCommand(command="/help", description="Help"),
            BotCommand(command="/info", description="Get info about yourself!"),
            BotCommand(command="/vacancy", description="E'lon berish")
        ]
    )

    dp.startup.register(start)
    dp.message.register(info, Command("info"))
    dp.message.register(help, Command("help"))
    dp.message.register(vacancy, Command("vacancy"))
    dp.message.register(register_name, SignUp.name)
    dp.message.register(register_phone, SignUp.phone)
    dp.message.register(register_location, SignUp.location)
    dp.message.register(register_position, SignUp.position)
    dp.message.register(register_finish, SignUp.salary)
    dp.message.register(bot_start, Command("start"))
    dp.shutdown.register(stop)
    await dp.start_polling(bot)


if __name__ == '__main__':
    run(main(dp))

