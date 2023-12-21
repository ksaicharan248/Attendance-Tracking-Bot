import base64
import concurrent.futures
import os
from aiogram.dispatcher.filters.state import State, StatesGroup
import threading
import io
import time
import pickle
from io import BytesIO
from PIL import Image
from aiogram import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ChatActions
import asyncio
from allop import goget, batchrolls ,graber ,length_of_subjects,search_by_name,bio_data
from todaypk import today, dato, today_rs
from webser import keep_alive
from tff import dft, parse_complex, idft
from re_feren_ce import key
import sympy

""" 
                                   data 
"""
bot = Bot(token=key)
dp = Dispatcher(bot)

lol_sub_total = length_of_subjects[0] - 2
lol_sub_total2 = length_of_subjects[1] - 2

calculator_mode = False
stop_event1 = threading.Event()
stop_event2 = threading.Event()

#                    recursvie fun
def update_attendance(stop_event) :
    while not stop_event.is_set() :
        total_attendance = graber()
        asyncio.run(gooo())
        if total_attendance is not False:
            with open('attendance_data.pkl' , 'wb') as file :
                pickle.dump(total_attendance , file)
            asyncio.run(gooo())
        time.sleep(600)

def stop_thread() -> None :
    stop_event2.set()

async def gooo() :

    with open('attendance_data.pkl' , 'rb') as file :
        total_attendance = pickle.load(file)
    with open('past_attendance_data.pkl' , 'rb') as file :
        intial = pickle.load(file)
    updated_list=[]
    if total_attendance[0][1] != intial :
        boont = Bot(token="6194712784:AAHa29JloERqh2RqYvPzTr5TJoCNeu28bzk")
        if intial[lol_sub_total]!=0:
            for i in range(0, lol_sub_total) :
                if total_attendance[0][1][i] != intial[i] :
                    if float(total_attendance[0][1][i]) > float(intial[i]) :
                        updated_list.append(total_attendance[0][0][i] + "  🔺 ")
                    else :
                        updated_list.append(total_attendance[0][0][i] + "  🔻 ")
            if len(updated_list)>0:
                await boont.send_message(chat_id="1746861239", text=' , '.join(updated_list),disable_notification=True)
        await boont.send_message(chat_id="1746861239", text="Attendance:" + str(total_attendance[0][1][lol_sub_total]) + "%",disable_notification=True)
        try :
            await boont.close()
        except DeprecationWarning as e:
            await boont.close()
        with open('past_attendance_data.pkl' , 'wb') as file :
            pickle.dump(total_attendance[0][1] , file)


#                             end

@dp.message_handler(commands=['updater'])
async def cmd_updaters(message: types.Message) :
    user_id = message.from_user.id
    if user_id == 1746861239 or user_id == 5139592059 :
        await bot.send_message(chat_id=message.chat.id, text="updating the process .....")
        rox = threading.Thread(target=update_attendance, args=(stop_event2,), name="secondary")
        rox.start()
        time.sleep(10)
        try :
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id + 1)
            await bot.send_message(chat_id=message.chat.id, text="updated suceesfully.....")
            time.sleep(5)
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id + 2)
        except Exception as e :
            pass
        if rox.is_alive() :
            timer = threading.Timer(100.0, stop_thread)
            timer.start()
    else :
        await bot.send_message(chat_id=message.chat.id,
                               text="You cannot use this commands this status is updated to admin")
        time.sleep(5)
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id + 1)


@dp.message_handler(commands=['start'])
async def start(message: types.Message) :
    await bot.send_message(chat_id=message.chat.id, text="Hello you need any help use,/help")


@dp.message_handler(commands=['help'])
async def help(message: types.Message) :
    await bot.send_message(chat_id=message.chat.id,
                           text="/attendance     --------->  percentage \n/allattendance --------->  including subjects\n/pic                    --------->  photo copy\n/more")


@dp.message_handler(commands=['more'])
async def cmd_more(message: types.Message) :
    await bot.send_message(chat_id=message.chat.id,text="/clear ---------->clear chat \n/todayattendance----->todays\n")
    try :
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception as e :
        pass


@dp.message_handler(commands=['attendance', 'a'])
async def attendance(message: types.Message) :
    with open('attendance_data.pkl' , 'rb') as file :
        total_attendance = pickle.load(file)
    if isinstance(total_attendance[0], str) :
        await bot.send_message(chat_id=message.chat.id, text="Server doesnt responded")

    else :
        if message.entities and len(message.entities) == 2 and message.entities[1].type == 'text_mention' :
            user_id = message.entities[1].user.id
        else :
            user_id = message.from_user.id
        if user_id == 1746861239 :
            t2 = total_attendance[0]
            await bot.send_message(chat_id=message.chat.id, text="your attendance is : " + str(t2[1][lol_sub_total]) + " %")
        elif user_id == 5139592059 :
            t2 = total_attendance[1]
            await bot.send_message(chat_id=message.chat.id, text="Your attendance is: " + str(t2[1][lol_sub_total2]) + " %")
        else :
            await bot.send_message(chat_id=message.chat.id, text="NO DATA EXISTS")


@dp.message_handler(commands='hey')
async def cmd_start(message: types.Message) :
    full_name = message.from_user.full_name
    if full_name is None :
        text = f"Hello! Glad to see you here!"
    else :
        text = f"Hello, {full_name}! Glad to see you here!"
    await bot.send_message(chat_id=message.chat.id, text=text)


@dp.message_handler(commands=['pic', 'p'])
async def pic(message: types.Message) :
    with open('attendance_data.pkl' , 'rb') as file :
        total_attendance = pickle.load(file)
    if isinstance(total_attendance[0], str) :
        await bot.send_message(chat_id=message.chat.id, text="Server doesnot responded")

    else :
        if message.entities and len(message.entities) == 2 and message.entities[1].type == 'text_mention' :
            user_id = message.entities[1].user.id
        else :
            user_id = message.from_user.id

        if user_id == 1746861239 :
            encoded_string = str(total_attendance[0][2])
            decoded_bytes = base64.b64decode(str(encoded_string))
            photo_file = io.BytesIO(decoded_bytes)
            chat_id = message.chat.id
            await message.bot.send_photo(chat_id=chat_id, photo=photo_file)
        elif user_id == 5139592059 :
            encoded_string = str(total_attendance[1][2])
            decoded_bytes = base64.b64decode(str(encoded_string))
            photo_file = io.BytesIO(decoded_bytes)
            chat_id = message.chat.id
            await message.bot.send_photo(chat_id=chat_id, photo=photo_file)
        else :
            await bot.send_message(chat_id=message.chat.id, text="NO DATA EXISTS")
        try :
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)
        except Exception as e :
            pass


@dp.message_handler(commands=['allattendance', 'atc'])
async def allattendance(message: types.Message) :
    with open('attendance_data.pkl' , 'rb') as file :
        total_attendance = pickle.load(file)
    if isinstance(total_attendance[0], str) :
        await bot.send_message(chat_id=message.chat.id, text="Server doesnt responded")

    else :
        if message.entities and len(message.entities) == 2 and message.entities[1].type == 'text_mention' :
            user_id = message.entities[1].user.id
        else :
            user_id = message.from_user.id

        if user_id == 1746861239 :
            t2 = total_attendance[0]
            await bot.send_message(chat_id=message.chat.id, text="subject" + " " * (16 - len("subject")) + " " + " " * (
                    7 - len(str("percentage"))) + "percentage " + "\n" + "\n".join(
                [str(t2[0][i]) + " " * (16 - len(str(t2[0][i]))) + ":" + " " * (7 - len(str(t2[1][i]))) + str(t2[1][i])
                 for
                 i in range(0, lol_sub_total+1)]))
        elif user_id == 5139592059 :

            t2 = total_attendance[1]
            await bot.send_message(chat_id=message.chat.id, text="subject" + " " * (16 - len("subject")) + " " + " " * (
                    7 - len(str("percentage"))) + "percentage " + "\n" + "\n".join(
                [str(t2[0][i]) + " " * (16 - len(str(t2[0][i]))) + ":" + " " * (7 - len(str(t2[1][i]))) + str(t2[1][i])
                 for
                 i in range(0, lol_sub_total2+1)]))
        else :
            await bot.send_message(chat_id=message.chat.id, text="NO data exists")

        try :
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)
        except Exception as e :
            pass


@dp.message_handler(commands=['todayattendance', 'tatc'])
async def cmd_toadyattendance(message: types.Message) :
    with open('attendance_data.pkl' , 'rb') as file :
        total_attendance = pickle.load(file)
    if isinstance(total_attendance[0], str) :
        await bot.send_message(chat_id=message.chat.id, text="Server doesnt responded")
    else :
        if message.entities and len(message.entities) == 2 and message.entities[1].type == 'text_mention' :
            user_id = message.entities[1].user.id
        else :
            user_id = message.from_user.id

        if user_id == 1746861239 :
            try :
                ref_dato = message.text.split()[1]
            except :
                ref_dato = ""
            date = dato(ref_dato)
            t2 = today(date)
            encoded_string = str(t2)
            decoded_bytes = base64.b64decode(str(encoded_string))
            photo_file = io.BytesIO(decoded_bytes)
            chat_id = message.chat.id
            await message.bot.send_photo(chat_id=chat_id, photo=photo_file)
        elif user_id == 5139592059 :
            try :
                ref_dato = message.text.split()[1]
            except :
                ref_dato = ""
            date = dato(ref_dato)
            t2 = today_rs(date)
            encoded_string = str(t2)
            decoded_bytes = base64.b64decode(str(encoded_string))
            photo_file = io.BytesIO(decoded_bytes)
            chat_id = message.chat.id
            await message.bot.send_photo(chat_id=chat_id, photo=photo_file)
        else :
            await bot.send_message(chat_id=message.chat.id, text="comming soon .....")
        try :
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)

        except Exception as e :
            pass


@dp.message_handler(commands=['timetable', 'tt'])
async def send_tt(message: types.Message) :
    if message.entities and len(message.entities) == 2 and message.entities[1].type == 'text_mention' :
        user_id = message.entities[1].user.id
    else :
        user_id = message.from_user.id

    if user_id == 1746861239 :
        photo_path = os.path.join(os.getcwd(), 'timetable.jpg')
        with Image.open(photo_path) as photo :
            photo_bytes = BytesIO()
            photo.save(photo_bytes, format='JPEG')
            photo_bytes.seek(0)
            await bot.send_photo(chat_id=message.chat.id, photo=photo_bytes)
    elif user_id == 5139592059 :
        photo_path = os.path.join(os.getcwd(), 'timetable1.jpg')
        with Image.open(photo_path) as photo :
            photo_bytes = BytesIO()
            photo.save(photo_bytes, format='JPEG')
            photo_bytes.seek(0)
            await bot.send_photo(chat_id=message.chat.id, photo=photo_bytes)
    else :
        photo_path = os.path.join(os.getcwd(), 'timetable.jpg')
        with Image.open(photo_path) as photo :
            photo_bytes = BytesIO()
            photo.save(photo_bytes, format='JPEG')
            photo_bytes.seek(0)
            await bot.send_photo(chat_id=message.chat.id, photo=photo_bytes)
    try :
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)
    except Exception as e :
        pass


@dp.message_handler(commands=['academic_calendar', 'ac', 'Ac', 'AC'])
async def send_academic_calendar(message: types.Message) :
    photo_path = os.path.join(os.getcwd(), 'clg.jpg')
    with Image.open(photo_path) as photo :
        photo_bytes = BytesIO()
        photo.save(photo_bytes, format='JPEG')
        photo_bytes.seek(0)
        await bot.send_photo(chat_id=message.chat.id, photo=photo_bytes)
    try :
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)
    except Exception as e :
        pass


@dp.message_handler(commands=['clear', 'clc','clr'])
async def cmd_clear(message: types.Message) :
    user_id = message.from_user.id
    if user_id == 1746861239 :
        try :
            ref_str_num = message.text.split()[1]
        except IndexError :
            ref_str_num = None
        if ref_str_num is None :
            ref_num = 50
        else :
            ref_num = int(ref_str_num)
        for i in range(0, ref_num) :
                try :
                    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - i)
                except Exception as e :
                    pass

    else :
        await bot.send_message(chat_id=message.chat.id, text="cant be used ")




@dp.message_handler(commands='roll')
async def i_pic(message: types.Message) :
    user_id = message.chat.id
    try :
        await message.bot.send_message(chat_id=message.chat.id , text="please wait for a while...")
        rollno = message.text.split()[1]
        with concurrent.futures.ThreadPoolExecutor(thread_name_prefix="roll_fuction") as ey :
            future = ey.submit(goget , rollno)
            encoded_string = future.result()
        decoded_bytes = base64.b64decode(str(encoded_string))
        photo_file = io.BytesIO(decoded_bytes)
        await message.bot.delete_message(chat_id=message.chat.id , message_id=message.message_id + 1)
        await message.bot.send_photo(chat_id=message.chat.id , photo=photo_file)
        try :
            await message.bot.delete_message(chat_id=message.chat.id , message_id=message.message_id - 1)
            await message.bot.delete_message(chat_id=message.chat.id , message_id=message.message_id - 2)
        except Exception as e :
            pass
    except Exception as e :
            await bot.send_message(chat_id=message.chat.id,
                                   text="Please enter last two digits of roll number, ex: roll xx .")




@dp.message_handler(commands=['batch', 'b'])
async def batchroll_num(message: types.Message) :
    start = time.time()
    thinking_msg = await message.answer("Moon 🌙 is thinking. 💭")
    with open("attendance.pkl" , "rb" ) as file :
        old_dict = pickle.load(file)
    t2 = batchrolls()
    x = long_running_function()
    for j in range(2) :
        for i in range(4) :
            dots = "." * (i + 2)
            await bot.edit_message_text(f"Moon 🌙 is thinking{dots} 💭" , chat_id=message.chat.id ,
                                        message_id=thinking_msg.message_id)
    if isinstance(t2, str) :
        await message.bot.delete_message(chat_id=message.chat.id , message_id=message.message_id + 1)
        await bot.send_message(chat_id=message.chat.id, text=t2)
    elif isinstance(t2, dict) :
        for roll_number in list(t2.keys()) :
            if roll_number in old_dict and roll_number in t2 :
                old_attendance = old_dict[roll_number]
                new_attendance = t2[roll_number]
                old_percentage: float = old_attendance.get("percentage")
                new_percentage: float = new_attendance.get("percentage")
                if old_percentage is not None and new_percentage is not None :
                    if float(new_percentage) > float(old_percentage) :
                        t2[roll_number]["state"] = "▲"
                    elif float(new_percentage) < float(old_percentage) :
                        t2[roll_number]["state"] = "🔻"
                    else :
                        t2[roll_number]["state"] = old_dict[roll_number]["state"]
        roll_no = list(t2.keys())
        percentage = [details['percentage'] for details in t2.values()]
        state = [details['state'] for details in t2.values()]
        t3 = [roll_no , percentage , state]
        output_lines = ["-> {0}     :      {1} %   {2}".format(t3[0][i] , t3[1][i] , t3[2][i]) for i in
                        range(len(t3[0]))]
        output_text = " roll num        percentage \n----------------------------------------\n" + "\n".join(
            output_lines)
        await message.bot.delete_message(chat_id=message.chat.id , message_id=thinking_msg.message_id)
        await bot.send_message(chat_id=message.chat.id , text=output_text)
        with open("attendance.pkl" , "wb") as file :
            pickle.dump(t2 , file)
    else:
        await message.bot.delete_message(chat_id=message.chat.id , message_id=message.message_id + 1)
        await bot.send_message(chat_id=message.chat.id, text="Nothing found..........")


@dp.message_handler(commands='find')
async def ioni_pic(message: types.Message) :
    await message.bot.send_message(chat_id=message.chat.id , text="Moon🌙 is thinking....")
    try :
        name = message.text.split()[1]
        with concurrent.futures.ThreadPoolExecutor(thread_name_prefix="search_by_name_fuction") as ey :
            future = ey.submit(search_by_name,name)
            encoded_string = future.result()
        decoded_bytes = base64.b64decode(str(encoded_string))
        photo_file = io.BytesIO(decoded_bytes)
        await message.bot.delete_message(chat_id=message.chat.id , message_id=message.message_id + 1)
        await message.bot.send_photo(chat_id=message.chat.id , photo=photo_file)

    except Exception as e:
        await message.bot.delete_message(chat_id=message.chat.id , message_id=message.message_id + 1)
        await message.bot.send_message(chat_id=message.chat.id,text="something need to be expected.")


@dp.message_handler(commands='bio')
async def bio_pic(message: types.Message):
    user_id = message.from_user.id
    if user_id :
        try :
            await message.bot.send_message(chat_id=message.chat.id , text="Moon🌙 is thinking....")
            rollnumber = message.text.split()[1]
            with concurrent.futures.ThreadPoolExecutor(thread_name_prefix="search_by_bio_fuction") as ey :
                future = ey.submit(bio_data , rollnumber)
                encoded_string = future.result()
            decoded_bytes = base64.b64decode(str(encoded_string))
            photo_file = io.BytesIO(decoded_bytes)
            await message.bot.delete_message(chat_id=message.chat.id , message_id=message.message_id + 1)
            await message.bot.send_photo(chat_id=message.chat.id , photo=photo_file)
        except Exception as e :
            await message.bot.delete_message(chat_id=message.chat.id , message_id=message.message_id + 1)
            await message.bot.send_message(chat_id=message.chat.id , text="something need to be expected.")
    else:
        await message.bot.delete_message(chat_id=message.chat.id , message_id=message.message_id + 1)
        await message.bot.send_message(chat_id=message.chat.id , text="Restricted by admin")


@dp.message_handler(commands=['input', 'in','i'])
async def update_message_handler(message: types.Message):
    await message.bot.delete_message(chat_id=message.chat.id , message_id=message.message_id )
    boont = Bot(token="6194712784:AAHa29JloERqh2RqYvPzTr5TJoCNeu28bzk")
    with open('attendance_data.pkl' , 'rb') as file :
        total_attendance = pickle.load(file)
    await boont.send_message(chat_id="1746861239", text="Attendance:" + str(total_attendance[0][1][lol_sub_total]) + "%",disable_notification=True)
def long_running_function():
    # Simulate a long-running tas
    asyncio.sleep(10)
    return "Task completed!"

@dp.message_handler(commands=['stat'])
async def cmd_start(message: types.Message):
    start = time.time()
    thinking_msg = await message.answer("Moon 🌙 is thinking. 💭")
    x = long_running_function()
    for j in range(2):
        for i in range(4) :
            dots = "." * (i + 2)
            await bot.edit_message_text(f"Moon 🌙 is thinking{dots} 💭" , chat_id=message.chat.id ,
                                        message_id=thinking_msg.message_id)

    await message.bot.delete_message(chat_id=message.chat.id , message_id=thinking_msg.message_id)
    stop = time.time()
    await message.answer(f'{x} \nTime taken: {stop - start:.2f} seconds')

'''
first_thread = threading.Thread(target=update_attendance, args=(stop_event1,), name="first")
first_thread.start()'''


if __name__ == '__main__' :
    keep_alive()
    executor.start_polling(dp)
