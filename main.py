import base64
import concurrent.futures
import os
import threading
import io
import time
from io import BytesIO
from PIL import Image
from aiogram import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
import asyncio
from allop import altho, altho_2, goget
from todaypk import today
from webser import keep_alive
from tff import dft, parse_complex, idft

bot = Bot(token="5751283716:AAGHgB6P15DPNyaV7Kr_FGQpbX0DjuUT0gc")
dp = Dispatcher(bot)

attendanc = ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 00000000)
roshitt = ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 00000000)


def update_attendance():
    while True:
        global attendanc, roshitt
        attendanc = altho()
        time.sleep(10)
        roshitt = altho_2()
        time.sleep(600)


@dp.message_handler(commands=['updater'])
async def cmd_updaters(message: types.Message):
    user_id = message.from_user.id
    if user_id == 1746861239:
        await bot.send_message(chat_id=message.chat.id, text="updating the process .....")
        r = threading.Thread(target=update_attendance)
        r.start()
        time.sleep(10)
        try:
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id + 1)
            await bot.send_message(chat_id=message.chat.id, text="updated suceesfully.....")
            time.sleep(5)
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id + 2)
        except Exception as e:
            pass
    else:
        await bot.send_message(chat_id=message.chat.id,
                               text="You cannot use this commands this status is updated to admin")
        time.sleep(5)
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id + 1)


@dp.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(chat_id=message.chat.id, text="Hello,/help")


@dp.message_handler(commands=['help'])
async def help(message):
    await bot.send_message(chat_id=message.chat.id,
                           text="/attendance---------> percentage\n/allattendance--------->including subjects "
                                "\n/pic------ > photo copy\n/more")


@dp.message_handler(commands=['more'])
async def cmd_more(message):
    await bot.send_message(chat_id=message.chat.id,
                           text="/clear ---------->clear chat \n/todayattendance----->todays\n")
    try:
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception as e:
        pass


@dp.message_handler(commands=['attendance', 'a'])
async def attendance(message: types.Message):
    global attendanc, roshitt
    if isinstance(attendanc, str):
        await bot.send_message(chat_id=message.chat.id, text="Server doesnt responded")

    else:
        if message.entities and len(message.entities) == 2 and message.entities[1].type == 'text_mention':
            user_id = message.entities[1].user.id
        else:
            user_id = message.from_user.id
        if user_id == 1746861239:
            t2 = attendanc
            await bot.send_message(chat_id=message.chat.id, text="your attendance is : " + str(t2[1][13]) + " %")
        else:
            t2 = roshitt
            await bot.send_message(chat_id=message.chat.id, text="Your attendance is: " + str(t2[1][12]) + " %")


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
    if isinstance(attendanc, str):
        await bot.send_message(chat_id=message.chat.id, text="Server doesnt responded")

    else:
        if message.entities and len(message.entities) == 2 and message.entities[1].type == 'text_mention':
            user_id = message.entities[1].user.id
        else:
            user_id = message.from_user.id

        if user_id == 1746861239:
            encoded_string = str(attendanc[2])
            decoded_bytes = base64.b64decode(str(encoded_string))
            photo_file = io.BytesIO(decoded_bytes)
            chat_id = message.chat.id
            await message.bot.send_photo(chat_id=chat_id, photo=photo_file)
        else:
            encoded_string = str(roshitt[2])
            decoded_bytes = base64.b64decode(str(encoded_string))
            photo_file = io.BytesIO(decoded_bytes)
            chat_id = message.chat.id
            await message.bot.send_photo(chat_id=chat_id, photo=photo_file)

        try:
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)
        except Exception as e:
            pass


@dp.message_handler(commands=['allattendance', 'atc'])
async def allattendance(message: types.Message):
    global attendanc, roshitt
    if isinstance(attendanc, str):
        await bot.send_message(chat_id=message.chat.id, text="Server doesnt responded")

    else:
        if message.entities and len(message.entities) == 2 and message.entities[1].type == 'text_mention':
            user_id = message.entities[1].user.id
        else:
            user_id = message.from_user.id

        if user_id == 1746861239:
            t2 = attendanc
            await bot.send_message(chat_id=message.chat.id, text="subject" + " " * (16 - len("subject")) + " " + " " * (
                    7 - len(str("percentage"))) + "percentage " + "\n" + "\n".join(
                [str(t2[0][i]) + " " * (16 - len(str(t2[0][i]))) + ":" + " " * (7 - len(str(t2[1][i]))) + str(t2[1][i])
                 for
                 i in range(0, 14)]))
        else:
            t2 = roshitt
            await bot.send_message(chat_id=message.chat.id, text="subject" + " " * (16 - len("subject")) + " " + " " * (
                    7 - len(str("percentage"))) + "percentage " + "\n" + "\n".join(
                [str(t2[0][i]) + " " * (16 - len(str(t2[0][i]))) + ":" + " " * (7 - len(str(t2[1][i]))) + str(t2[1][i])
                 for
                 i in range(0, 13)]))

        try:
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)
        except Exception as e:
            pass


@dp.message_handler(commands=['todayattendance', 'tatc'])
async def cmd_toadyattendance(message: types.Message):
    if isinstance(attendanc, str):
        await bot.send_message(chat_id=message.chat.id, text="Server doesnt responded")

    else:
        if message.entities and len(message.entities) == 2 and message.entities[1].type == 'text_mention':
            user_id = message.entities[1].user.id
        else:
            user_id = message.from_user.id

        if user_id == 1746861239:
            t2 = today()
            await bot.send_message(chat_id=message.chat.id,
                                   text="CS           :" + str(t2[0]) + "\n" + "EMTL      :" + str(
                                       t2[1]) + "\n" + "VLSI         :" + str(t2[2]) + "\n" + "EMI          :" + str(
                                       t2[3]) + "\n" + "IR             :" + str(t2[4]) + "\n" + "MAP        :" + str(
                                       t2[5]) + "\n" + "CS LAB    :" + str(t2[6]) + "\n" + "VL LAB    :" + str(
                                       t2[7]) + "\n" + "COI          :" + str(
                                       t2[8]) + "\n" + "CONS      :" + str(t2[9]) + "\n" + "LIB           :" + str(
                                       t2[10]) + "\n" + "TOTAL     :" + str(t2[11]) + "%")

        else:
            await bot.send_message(chat_id=message.chat.id, text="comming soon .....")
        try:
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)
        except Exception as e:
            pass


@dp.message_handler(commands=['timetable', 'tt'])
async def send_tt(message: types.Message):
    if message.entities and len(message.entities) == 2 and message.entities[1].type == 'text_mention':
        user_id = message.entities[1].user.id
    else:
        user_id = message.from_user.id

    if user_id == 1746861239:
        photo_path = os.path.join(os.getcwd(), 'timetable.jpg')
        with Image.open(photo_path) as photo:
            photo_bytes = BytesIO()
            photo.save(photo_bytes, format='JPEG')
            photo_bytes.seek(0)
            await bot.send_photo(chat_id=message.chat.id, photo=photo_bytes)
    else:
        photo_path = os.path.join(os.getcwd(), 'timetable1.jpg')
        with Image.open(photo_path) as photo:
            photo_bytes = BytesIO()
            photo.save(photo_bytes, format='JPEG')
            photo_bytes.seek(0)
            await bot.send_photo(chat_id=message.chat.id, photo=photo_bytes)

    try:
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)
    except Exception as e:
        pass


@dp.message_handler(commands=['academic_calendar', 'ac', 'Ac', 'AC'])
async def send_academic_calendar(message: types.Message):
    photo_path = os.path.join(os.getcwd(), 'clg.jpg')
    with Image.open(photo_path) as photo:
        photo_bytes = BytesIO()
        photo.save(photo_bytes, format='JPEG')
        photo_bytes.seek(0)
        await bot.send_photo(chat_id=message.chat.id, photo=photo_bytes)
    try:
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)
    except Exception as e:
        pass


@dp.message_handler(commands=['clear', 'clc', 'clr'])
async def cmd_clear(message: types.Message):
    full_name = str(message.from_user.first_name) + str(message.from_user.last_name)
    if full_name == "saicharan":
        for i in range(0, 50):
            try:
                await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - i)
            except Exception as e:
                pass
    else:
        await bot.send_message(chat_id=message.chat.id, text="cant be used ")


@dp.message_handler(commands=['dft'])
async def dft_handler(message: types.Message):
    try:
        input_str = message.text.split()[1]
        input_list = input_str.split(",")
        x = [parse_complex(val) for val in input_list]
        y = dft(x)
        await bot.send_message(chat_id=message.chat.id, text='\n'.join(str(val) for val in y))
    except Exception as e:
        await bot.send_message(chat_id=message.chat.id, text='Bad sequence ')


@dp.message_handler(commands=['idft'])
async def idft_handler(message: types.Message):
    try:
        input_str = message.text.split()[1]
        input_list = input_str.split(",")
        x = [parse_complex(val) for val in input_list]
        y = idft(x)
        await bot.send_message(chat_id=message.chat.id, text='\n'.join(str(val) for val in y))
    except Exception as e:
        await bot.send_message(chat_id=message.chat.id, text='Bad sequence ')


@dp.message_handler(commands='roll')
async def pic(message: types.Message):

    if isinstance(attendanc, str):
        await bot.send_message(chat_id=message.chat.id, text="Server doesnt responded")

    else:
        rollno = message.text.split()[1]
        with concurrent.futures.ThreadPoolExecutor() as ey:
            future = ey.submit(goget, rollno)
            encoded_string = future.result()
        decoded_bytes = base64.b64decode(str(encoded_string))
        photo_file = io.BytesIO(decoded_bytes)
        chat_id = message.chat.id
        await message.bot.send_photo(chat_id=chat_id, photo=photo_file)
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
