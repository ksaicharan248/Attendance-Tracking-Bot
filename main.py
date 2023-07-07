import base64
import concurrent.futures
import os
import threading
import io
import time
import pickle
from io import BytesIO
from PIL import Image
from aiogram import *
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from allop import altho, altho_2, goget, batchrolls ,graber
from todaypk import today, dato, today_rs
from webser import keep_alive
from tff import dft, parse_complex, idft
from re_feren_ce import key
import sympy

bot = Bot(token=key)
dp = Dispatcher(bot)
intial =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
attendanc = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 00000000]
roshitt = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 00000000]
calculator_mode = False
stop_event1 = threading.Event()
stop_event2 = threading.Event()


def update_attendance(stop_event) :
    while not stop_event.is_set() :
        global attendanc, roshitt
        total_attendance = graber()
        attendanc = total_attendance[0]
        roshitt = total_attendance[1]
        asyncio.run(gooo())
        time.sleep(600)



def stop_thread() -> None :
    stop_event2.set()


async def gooo() :
    global intial, attendanc
    updated_list=[]
    t = attendanc[1]
    if t != intial :
        boont = Bot(token="6194712784:AAHa29JloERqh2RqYvPzTr5TJoCNeu28bzk")
        if intial[13]!=0:
            for i in range(0, 13) :
                if t[i] != intial[i] :
                    if float(t[i]) > float(intial[i]) :
                        updated_list.append(attendanc[0][i] + "  ⬆️ ")
                    else :
                        updated_list.append(attendanc[0][i] + "  ⬇️ ")
            if len(updated_list)>0:
                await boont.send_message(chat_id="1746861239", text=' , '.join(updated_list),disable_notification=True)
        await boont.send_message(chat_id="1746861239", text="Attendance:" + str(t[13]) + "%",disable_notification=True)
        try :
            await boont.close()
        except DeprecationWarning as e:
            await boont.close()

        intial = t




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
    await bot.send_message(chat_id=message.chat.id, text="Hello,/help")


@dp.message_handler(commands=['help'])
async def help(message: types.Message) :
    await bot.send_message(chat_id=message.chat.id,
                           text="/attendance     --------->  percentage \n/allattendance --------->  including subjects\n/pic                    --------->  photo copy\n/more")


@dp.message_handler(commands=['more'])
async def cmd_more(message: types.Message) :
    await bot.send_message(chat_id=message.chat.id,
                           text="/clear ---------->clear chat \n/todayattendance----->todays\n")
    try :
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception as e :
        pass


@dp.message_handler(commands=['attendance', 'a'])
async def attendance(message: types.Message) :
    global attendanc, roshitt
    if isinstance(attendanc, str) :
        await bot.send_message(chat_id=message.chat.id, text="Server doesnt responded")

    else :
        if message.entities and len(message.entities) == 2 and message.entities[1].type == 'text_mention' :
            user_id = message.entities[1].user.id
        else :
            user_id = message.from_user.id
        if user_id == 1746861239 :
            t2 = attendanc
            await bot.send_message(chat_id=message.chat.id, text="your attendance is : " + str(t2[1][13]) + " %")
        elif user_id == 5139592059 :
            t2 = roshitt
            await bot.send_message(chat_id=message.chat.id, text="Your attendance is: " + str(t2[1][12]) + " %")
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


@dp.message_handler(commands='pic')
async def pic(message: types.Message) :
    global attendanc, roshitt
    if isinstance(attendanc, str) :
        await bot.send_message(chat_id=message.chat.id, text="Server doesnt responded")

    else :
        if message.entities and len(message.entities) == 2 and message.entities[1].type == 'text_mention' :
            user_id = message.entities[1].user.id
        else :
            user_id = message.from_user.id

        if user_id == 1746861239 :
            encoded_string = str(attendanc[2])
            decoded_bytes = base64.b64decode(str(encoded_string))
            photo_file = io.BytesIO(decoded_bytes)
            chat_id = message.chat.id
            await message.bot.send_photo(chat_id=chat_id, photo=photo_file)
        elif user_id == 5139592059 :
            encoded_string = str(roshitt[2])
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
    global attendanc, roshitt
    if isinstance(attendanc, str) :
        await bot.send_message(chat_id=message.chat.id, text="Server doesnt responded")

    else :
        if message.entities and len(message.entities) == 2 and message.entities[1].type == 'text_mention' :
            user_id = message.entities[1].user.id
        else :
            user_id = message.from_user.id

        if user_id == 1746861239 :
            t2 = attendanc
            await bot.send_message(chat_id=message.chat.id, text="subject" + " " * (16 - len("subject")) + " " + " " * (
                    7 - len(str("percentage"))) + "percentage " + "\n" + "\n".join(
                [str(t2[0][i]) + " " * (16 - len(str(t2[0][i]))) + ":" + " " * (7 - len(str(t2[1][i]))) + str(t2[1][i])
                 for
                 i in range(0, 14)]))
        elif user_id == 5139592059 :

            t2 = roshitt
            await bot.send_message(chat_id=message.chat.id, text="subject" + " " * (16 - len("subject")) + " " + " " * (
                    7 - len(str("percentage"))) + "percentage " + "\n" + "\n".join(
                [str(t2[0][i]) + " " * (16 - len(str(t2[0][i]))) + ":" + " " * (7 - len(str(t2[1][i]))) + str(t2[1][i])
                 for
                 i in range(0, 13)]))
        else :
            await bot.send_message(chat_id=message.chat.id, text="NO data exists")

        try :
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)
        except Exception as e :
            pass


@dp.message_handler(commands=['todayattendance', 'tatc'])
async def cmd_toadyattendance(message: types.Message) :
    if isinstance(attendanc, str) :
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
        if full_name == "saicharan" :
            for i in range(0, ref_num) :
                try :
                    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - i)
                except Exception as e :
                    pass

    else :
        await bot.send_message(chat_id=message.chat.id, text="cant be used ")



@dp.message_handler(commands=['dft'])
async def dft_handler(message: types.Message) :
    try : 
        input_list = input_str.split(",")
        x = [parse_complex(val) for val in input_list]
        y = dft(x)
        await bot.send_message(chat_id=message.chat.id, text='\n'.join(str(val) for val in y))
    except Exception as e :
        await bot.send_message(chat_id=message.chat.id, text='Bad sequence ')


@dp.message_handler(commands=['idft'])
async def idft_handler(message: types.Message) :
    try :
        input_str = message.text.split()[1]
        input_list = input_str.split(",")
        x = [parse_complex(val) for val in input_list]
        y = idft(x)
        await bot.send_message(chat_id=message.chat.id, text='\n'.join(str(val) for val in y))
    except Exception as e :
        await bot.send_message(chat_id=message.chat.id, text='Bad sequence ')


@dp.message_handler(commands='roll')
async def i_pic(message: types.Message) :
    user_id = message.chat.id
    try :
            rollno = message.text.split()[1]
            with concurrent.futures.ThreadPoolExecutor(thread_name_prefix="roll_fuction") as ey :
                future = ey.submit(goget, rollno)
                encoded_string = future.result()
            decoded_bytes = base64.b64decode(str(encoded_string))
            photo_file = io.BytesIO(decoded_bytes)
            await message.bot.send_photo(chat_id=message.chat.id, photo=photo_file)
            try :
                await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
                await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)
            except Exception as e :
                pass

    except Exception as e :
            await bot.send_message(chat_id=message.chat.id,
                                   text="Please enter last two digits of roll number, ex: roll xx .")


@dp.message_handler(commands=['calc'])
async def start_calculator(message: types.Message) :
    global calculator_mode
    calculator_mode = True
    await message.reply('Calculator mode started. Please enter a calculation. Use /stopcalc to exit calculator mode.')


@dp.message_handler(commands=['stopcalc'])
async def stop_calculator(message: types.Message) :
    global calculator_mode
    calculator_mode = False
    await message.reply('Calculator mode stopped./calc')


@dp.message_handler(lambda message : calculator_mode and not message.text.startswith('/'))
async def calculate(message: types.Message) :
    calculation = message.text
    try :
        result = sympy.sympify(calculation)
        try :
            num = float(result.evalf())
            await message.reply(str(num))
        except :
            await message.reply(str(result))


    except sympy.SympifyError :
        await bot.send_message(chat_id=message.chat.id, text="i dont even understand...")


@dp.message_handler(commands='batch')
async def batchroll_num(message: types.Message) :
    with open("attendance.pkl" , "rb") as file :
        old_dict = pickle.load(file)

    t2 = batchrolls()
    for roll_number in list(t2.keys()) :
        if roll_number in old_dict and roll_number in t2 :
            old_attendance = old_dict[roll_number]
            new_attendance = t2[roll_number]
            old_percentage :float = old_attendance.get("percentage")
            new_percentage :float= new_attendance.get("percentage")
            if old_percentage is not None and new_percentage is not None :
                if float(new_percentage) > float(old_percentage):
                    t2[roll_number]["state"] = "▲"
                elif float(new_percentage) < float(old_percentage):
                    t2[roll_number]["state"] = "🔻"
                else :
                    t2[roll_number]["state"] = old_dict[roll_number]["state"]
    t4 = list(t2.keys())
    name = [details['percentage'] for details in t2.values()]
    percentage = [details['state'] for details in t2.values()]
    t3 = [t4 , name , percentage]
    await bot.send_message(chat_id=message.chat.id,
                           text =".    roll num " + " " * (
                                           15 - len("roll num")) + " " + " " * (
                                                7 - len(str("percentage"))) + "percentage " + "\n" +"----------------------------------------\n" +"\n".join(
                                       ["-> "+str(t3[0][i]) + " " * (
                                               13 - len(str(t3[0][i]))) + ":" + " " * (
                                                10 - len(str(t3[1][i]))) + str(t3[1][i]) + " %" + " " * (10 - len(str(t3[1][i]))) +str(t3[2][i])
                                        for
                                        i in range(0, len(t3[0]))]))
    with open("attendance.pkl" , "wb") as file :
        pickle.dump(t2, file)


first_thread = threading.Thread(target=update_attendance, args=(stop_event1,), name="first")
first_thread.start()

if __name__ == '__main__' :
    keep_alive()
    executor.start_polling(dp)
