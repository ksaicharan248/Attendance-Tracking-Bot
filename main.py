import base64
import threading
import io
import time
from aiogram import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
import asyncio
from allop import altho, altho_2
from webser import keep_alive

bot = Bot(token="5751283716:AAGHgB6P15DPNyaV7Kr_FGQpbX0DjuUT0gc")
dp = Dispatcher(bot)

attendanc = ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0000 )
roshitt = ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0000)


def update_attendance():
    while True:
        global attendanc, roshitt
        attendanc = altho()
        time.sleep(10)
        roshitt = altho_2()
        time.sleep(1800)


@dp.message_handler(commands=['start'])
async def start(message):
    # Send a message to the user
    await bot.send_message(chat_id=message.chat.id, text="Hello,/help")

@dp.message_handler(commands=['help'])
async def help(message):
    # Send a message to the user
    await bot.send_message(chat_id=message.chat.id, text="attendance")

@dp.message_handler(commands=['attendance'])
async def attendance(message: types.Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    full_name = str(message.from_user.first_name) + str(message.from_user.last_name)
    global attendanc, roshitt

    if chat_id == 1746861239 or full_name == "saicharan":
        t2 = attendanc
        await message.reply("your attendance is : " + str(t2[1][11]) + " %")
    else:
        t2 = roshitt
        await message.reply("Your attendance is: " + str(t2[1][11]) + " %")


@dp.message_handler(commands='hey')
async def cmd_start(message: types.Message):
    full_name = message.from_user.full_name
    if full_name is None:
        text = f"Hello! Glad to see you here!"
    else:
        text = f"Hello, {full_name}! Glad to see you here!"
    await bot.send_message(chat_id=message.chat.id, text=text)


@dp.message_handler(commands='pic')
async def pic(message: types.Message):
    global attendanc, roshitt
    chat_id = message.chat.id
    user_id = message.from_user.id
    full_name = str(message.from_user.first_name) + str(message.from_user.last_name)
    if full_name == "saicharan":
        encoded_string = str(attendanc[2])
        decoded_bytes = base64.b64decode(str(encoded_string))
        photo_file = io.BytesIO(decoded_bytes)
        chat_id = message.chat.id
        await message.bot.send_photo(chat_id=chat_id, photo=photo_file)
    else:
        encoded_string = str(roshitt[2])
        decoded_bytes = base64.b64decode(encoded_string)
        photo_file = io.BytesIO(decoded_bytes)
        chat_id = message.chat.id
        await message.bot.send_photo(chat_id=chat_id, photo=photo_file)

    try:
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)
    except Exception as e:
        pass

@dp.message_handler(commands='allattendance')
async def allattendance(message: types.Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    full_name = str(message.from_user.first_name) + str(message.from_user.last_name)
    global attendanc, roshitt
    if chat_id == 1746861239 or full_name == "saicharan":
        t2 = attendanc
        await message.reply("subject" + " " * (16-len("subject")) + " " + " " * (7-len(str("percentage"))) + "percentage " + "\n" + "\n".join([str(t2[0][i]) + " " * (16-len(str(t2[0][i]))) + ":" + " " * (7-len(str(t2[1][i]))) + str(t2[1][i]) for i in range(0,12)]))
    else:
        t2 = roshitt
        await message.reply("subject" + " " * (16-len("subject")) + " " + " " * (7-len(str("percentage"))) + "percentage " + "\n" + "\n".join([str(t2[0][i]) + " " * (16-len(str(t2[0][i]))) + ":" + " " * (7-len(str(t2[1][i]))) + str(t2[1][i]) for i in range(0,12)]))

    try:
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)
    except Exception as e:
        pass

t = threading.Thread(target=update_attendance)
t.start()

keep_alive()
if __name__ == '__main__':
    executor.start_polling(dp)

