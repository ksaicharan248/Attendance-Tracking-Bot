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
from aiogram.types import ParseMode
import asyncio
from allop import goget, batchrolls ,graber ,length_of_subjects,search_by_name,bio_data,batch_data
from todaypk import today, dato, today_rs
from webser import keep_alive
from tff import dft, parse_complex, idft
from re_feren_ce import key
import sympy
from PIL import Image, ImageDraw, ImageFont
import requests
import textwrap
import google.generativeai as palm


""" 
                                   data 
"""
bot = Bot(token=key)
dp = Dispatcher(bot)

lol_sub_total = length_of_subjects[0] - 2
lol_sub_total2 = length_of_subjects[1] - 2

stop_event1 = threading.Event()
stop_event2 = threading.Event()


API_KEY = "AIzaSyDv6b2d3jyi93_rxLw_eb9Ab9CQedyt3XM"
palm.configure(api_key=API_KEY)
model = palm.GenerativeModel('gemini-pro')
chater = model.start_chat(history=[])
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
        await message.bot.send_message(chat_id=message.chat.id , text="Moon 🌙 is thinking...💭")
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
    thinking_msg = await message.answer("Moon 🌙 is thinking...💭")
    with open("attendance.pkl" , "rb" ) as file :
        old_dict = pickle.load(file)
    t2 = batchrolls()
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


@dp.message_handler(commands=['bp','pb','batchfa'])
async def batchpic(message: types.Message):
    thinking_msg = await message.answer("Moon 🌙 is thinking...💭")
    with open("attendance.pkl" , "rb") as file :
        old_dict = pickle.load(file)
    t2 = batch_data()
    if isinstance(t2 , str) :
        await message.bot.delete_message(chat_id=message.chat.id , message_id=message.message_id + 1)
        await bot.send_message(chat_id=message.chat.id , text=t2)
    elif isinstance(t2 , dict) :
        roll_no = list(t2.keys())
        percentage = [details['percentage'] for details in t2.values()]
        t3 = [roll_no , percentage ]
        output_lines = ["-> {0}     :      {1} % ".format(t3[0][i] , t3[1][i]) for i in
                        range(len(t3[0]))]
        output_text = " roll num        percentage \n----------------------------------------\n" + "\n".join(
            output_lines)
        await message.bot.delete_message(chat_id=message.chat.id , message_id=thinking_msg.message_id)
        await bot.send_message(chat_id=message.chat.id , text=output_text)
    else :
        await message.bot.delete_message(chat_id=message.chat.id , message_id=message.message_id + 1)
        await bot.send_message(chat_id=message.chat.id , text="Nothing found..........")







def create_table(draw, headers, data, start_position, cell_width, cell_height, header_font, data_font):
    # Dark theme colors
    background_color = "#1A1C28"
    text_color = "white"
    header_color = "#1A1C28"
    line_color = "gray"
    x, y = start_position
    for i, header in enumerate(headers):
        draw.rectangle([x, y, x + cell_width[i], y + cell_height], fill=header_color)
        draw.text((x + 5, y + 5), header, font=header_font, fill=text_color)
        x += cell_width[i]
    y += cell_height
    for roll_number, details in data.items():
        x = start_position[0]
        draw.rectangle([x, y, x + cell_width[0], y + cell_height], fill=background_color)
        draw.text((x + 5, y + 5), str(roll_number), font=data_font, fill=text_color)
        x += cell_width[0]
        for key in ['name', 'percentage']:  # Exclude the "state" key
            draw.rectangle([x, y, x + cell_width[1], y + cell_height], fill=background_color)
            if key == 'percentage':
                draw.text((x + 5, y + 5), f"{details[key]} %", font=data_font, fill=text_color)
            else:
                draw.text((x + 5, y + 5), str(details[key]), font=data_font, fill=text_color)
            x += cell_width[1]
            draw.line([(x, y), (x, y + cell_height)], fill=line_color, width=1)
        y += cell_height

# Command handler for the "/table" command
@dp.message_handler(commands=['table'])
async def send_table(message: types.Message):
    # Create a blank image
    image_width = 550
    image_height = 510
    image = Image.new("RGB", (image_width, image_height), "#1A1C28")
    draw = ImageDraw.Draw(image)
    header_font = ImageFont.truetype("type1.ttf", 16)  # Replace "path_to_header_font.ttf" with your font file
    data_font = ImageFont.truetype("type2.ttf", 14)  # Replace "path_to_data_font.ttf" with your font file
    cell_width = [150, 200, 150]  # Adjust widths as needed
    cell_height = 30
    headers = ["Roll number", "Name", "Percentage"]
    data = batch_data()
    table_start_position = (50, 50)
    create_table(draw, headers, data, table_start_position, cell_width, cell_height, header_font, data_font)
    image_buffer = io.BytesIO()
    image.save(image_buffer, format='PNG')
    image_buffer.seek(0)
    with image_buffer as photo:
        await message.bot.send_photo(chat_id=message.chat.id , photo=image_buffer)




def to_markdown(text):
    text = text.replace('•', '  *')
    indented_text = textwrap.indent(text, ' ', predicate=lambda _: True)
    return indented_text

@dp.message_handler(commands=['analyze','ana'])
async def send_data(message: types.Message):
    with open('attendance_data.pkl' , 'rb') as file :
        total_attendance = pickle.load(file)
    filtered_attendance_data = {key : float(value) for key , value in zip(total_attendance[0][0] , total_attendance[0][1]) if value != 0.0}
    zipped_data = {key : value for key , value in filtered_attendance_data.items() if value != 0.0}
    try:
        prompt_text = f"{message.text.split()[1]} ,This is my attendance data {zipped_data} you can analyze this data"
    except:
        prompt_text = f"I would like to analyze my attendance for the following classes: {zipped_data}. Please suggest which classes I should attend, explain clearly which ones I can skip, and provide a probability percentage for taking leave from a specific class"
    api_key = "AIzaSyCexfS8zCMI_mlyswWf7k3LSO-uOq8ebgE"
    gemini_api_endpoint = "https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText?key={API_KEY}"
    request_body = {"prompt" : {"text" : prompt_text}}
    response = requests.post(gemini_api_endpoint.format(API_KEY=api_key) , json=request_body)
    if response.status_code == 200 :
        generated_text = response.json()["candidates"][0]["output"]
        output = to_markdown(generated_text)
    else :
        output = "An error occurred while sending the request to the Gemini API."
    await bot.send_message(chat_id=message.chat.id , text=output, parse_mode=ParseMode.MARKDOWN)



gpt_mode = False
@dp.message_handler(commands=['gpt'])
async def start_calculator(message: types.Message) :
    global gpt_mode
    gpt_mode = True
    await message.reply('gpt mode started. please enter a promt. Use /stopgpt to exit gpt mode.')


@dp.message_handler(commands=['stopgpt'])
async def stop_calculator(message: types.Message) :
    global gpt_mode
    gpt_mode = False
    await message.reply('Gpt mode stopped./gpt to start again')


@dp.message_handler(lambda message : gpt_mode and not message.text.startswith('/'))
async def calculate(message: types.Message) :
    if message.reply_to_message and is_user_message :
        user_input = message.reply_to_message.text
    else :
        user_input = message.text
    api_key = "AIzaSyCexfS8zCMI_mlyswWf7k3LSO-uOq8ebgE"
    gemini_api_endpoint = "https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText?key={API_KEY}"
    request_body = {"prompt" : {"text" : user_input}}
    response = requests.post(gemini_api_endpoint.format(API_KEY=api_key) , json=request_body)
    if response.status_code == 200 :
        generated_text = response.json()["candidates"][0]["output"]
        output = to_markdown(generated_text)
    else :
        output = "An error occurred while sending the request to the Gemini API."
    await bot.send_message(chat_id=message.chat.id , text=output, parse_mode=ParseMode.MARKDOWN)

talk_mode = False

@dp.message_handler(commands=['talk'])
async def talk(message: types.Message) :
    global talk_mode
    talk_mode= True
    await bot.send_message(chat_id=message.chat.id , text="talk mode started. please enter a promt. Use /stoptalk to exit talk mode.")

@dp.message_handler(commands=['stoptalk'])
async def stop_talk(message: types.Message) :
    global talk_mode
    talk_mode = False
    chater.history.clear()
    await bot.send_message(chat_id=message.chat.id , text="Talk mode stopped. /talk to start again.")

@dp.message_handler(lambda message : talk_mode and not message.text.startswith('/'))
async def talk_back(message: types.Message) :
    global talk_mode
    if message.reply_to_message and is_user_message :
        user_input = message.reply_to_message.text
    else :
        user_input = message.text
    response = chater.send_message(user_input)
    await message.bot.send_message(chat_id=message.chat.id , text=response.text,parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['id_only'])
async def id_only(message: types.Message) :
    await bot.send_message(chat_id=message.chat.id , text=f'{message.from_user.id}\n{message.chat.id}')




first_thread = threading.Thread(target=update_attendance, args=(stop_event1), name="first")
first_thread.start()


if __name__ == '__main__' :
    keep_alive()
    executor.start_polling(dp)