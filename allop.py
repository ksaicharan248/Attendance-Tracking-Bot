import asyncio
from aiogram import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from PIL import Image
import io
import base64
import time

length_of_subjects = [14 , 14]


def goget(x) :
    try :
        y = str(x)
        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=opt)
        driver.set_window_size(1024 , 768)
        driver.get("http://bit.ly/3Qb3MoX")
        driver.get("http://bit.ly/3Qb3MoX")
        driver.get("http://117.239.51.140/sitams/Academics/StudentAttendance.aspx?")
        if len(y) == 2 :
            driver.find_element(By.CSS_SELECTOR , '#txtRollNo').send_keys("20751A04" + y)
        elif 'l' in y :
            n = y.replace("l" , "")
            driver.find_element(By.CSS_SELECTOR , '#txtRollNo').send_keys("21755a04" + n)
        elif 'l' not in y and len(y) == 3 :
            driver.find_element(By.CSS_SELECTOR , '#txtRollNo').send_keys("20751a0" + y)
        driver.find_element(By.CSS_SELECTOR , '#radTillNow').click()
        driver.find_element(By.CSS_SELECTOR , '#btnShow').click()
        div_element = driver.find_element('css selector' , '#tblReport')
        driver.execute_script(f'document.querySelector("#tblReport").style.height ="510px";')
        screenshot = div_element.screenshot_as_png
        image = Image.open(io.BytesIO(screenshot)).convert('RGB')
        with io.BytesIO() as output :
            image.save(output , format='JPEG')
            image_bytes = output.getvalue()
        encoded_string = base64.b64encode(image_bytes).decode('utf-8')
        driver.close()
        return encoded_string

    except WebDriverException :
        return 'server not responding 404'


def graber() :
    try :
        global length_of_subjects
        roll_numbers = ['20751A0467' , '20751A0232']
        roll_data = []
        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=opt)
        driver.set_window_size(1024 , 768)
        driver.get("http://bit.ly/3Qb3MoX")
        driver.get("http://bit.ly/3Qb3MoX")
        driver.get("http://117.239.51.140/sitams/Academics/StudentAttendance.aspx?")
        for x in range(len(roll_numbers)) :
            subjects , results , txt = [] , [] , []
            driver.find_element(By.CSS_SELECTOR , '#txtRollNo').send_keys(roll_numbers[x])
            driver.find_element(By.CSS_SELECTOR , '#radTillNow').click()
            driver.find_element(By.CSS_SELECTOR , '#btnShow').click()
            for i in range(2 , length_of_subjects[x]) :
                selectors = [
                    "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child({}) > td:nth-child({})".format(
                        i , col) for col in [2 , 5]]
                values = [driver.find_element(By.CSS_SELECTOR , selector).text for selector in selectors]
                subjects.append(values[0])
                results.append(values[1])
            txt = [driver.find_element(By.CSS_SELECTOR ,
                                       "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child({}) > td:nth-child({})".format(
                                           length_of_subjects[x] , i)).text for i in [1 , 4]]
            subjects.append(txt[0])
            results.append(txt[1])
            div_element = driver.find_element('css selector' , '#tblReport')
            if x == 0 :
                driver.execute_script(f'document.querySelector("#tblReport").style.height ="510px";')
            screenshot = div_element.screenshot_as_png
            image = Image.open(io.BytesIO(screenshot)).convert('RGB')
            with io.BytesIO() as output :
                image.save(output , format='PNG' , quality=100)
                image_bytes = output.getvalue()
            encoded_string = base64.b64encode(image_bytes).decode('utf-8')
            roll_data.append([subjects , results , encoded_string])
            driver.find_element(By.CSS_SELECTOR , '#txtRollNo').clear()

        driver.close()
        return roll_data


    except WebDriverException as e :
        return False


def batchrolls() :
    try :
        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=opt)
        driver.set_window_size(1024 , 768)
        driver.get("http://bit.ly/3Qb3MoX")
        driver.get("http://bit.ly/3Qb3MoX")
        driver.get("http://117.239.51.140/sitams/Academics/StudentAttendance.aspx?")
        batche = {'462' : {'percentage' : 0 , 'state' : ''} , '464' : {'percentage' : 0 , 'state' : ''} ,
                  '467' : {'percentage' : 0 , 'state' : ''} , '469' : {'percentage' : 0 , 'state' : ''} ,
                  '478' : {'percentage' : 0 , 'state' : ''} , '483' : {'percentage' : 0 , 'state' : ''} ,
                  '486' : {'percentage' : 0 , 'state' : ''} , '491' : {'percentage' : 0 , 'state' : ''} ,
                  '4A3' : {'percentage' : 0 , 'state' : ''} , '4A5' : {'percentage' : 0 , 'state' : ''} ,
                  '4B1' : {'percentage' : 0 , 'state' : ''} , '408' : {'percentage' : 0 , 'state' : ''} ,
                  '407' : {'percentage' : 0 , 'state' : ''} , '412' : {'percentage' : 0 , 'state' : ''}}

        roll_numbers = list(batche.keys())
        for i in range(len(roll_numbers)) :
            roll_number = roll_numbers[i]
            roll_string = "20751A0" + str(roll_number) if i < 11 else "21755A0" + str(roll_number)
            driver.find_element(By.CSS_SELECTOR , '#txtRollNo').send_keys(roll_string)
            driver.find_element(By.CSS_SELECTOR , '#radTillNow').click()
            driver.find_element(By.CSS_SELECTOR , '#btnShow').click()
            res = driver.find_element(By.CSS_SELECTOR ,
                                      "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(14) > td:nth-child(4)").text
            batche[roll_number]['percentage'] = res
            driver.find_element(By.CSS_SELECTOR , '#txtRollNo').clear()

        sorted_batche = dict(sorted(batche.items() , key=lambda x : x[1]['percentage'] , reverse=True))
        return sorted_batche

    except WebDriverException :

        return "Error occurred during web scraping."


if __name__ == "__main__" :
    start_time = time.time()


    async def getoo() :
        s = 3 #int(input("enter the option 1,2,3,4:-------->"))
        bot = Bot(token='5647188009:AAGrRZA8fuY0il7LjY2WJ-EJuEhb809M4zU')
        if s == 1 :
            attend = graber()
            for k in range(0 , 2) :
                t2 = attend[k]

                decoded_bytes = base64.b64decode(str(t2[2]))
                photo_file = io.BytesIO(decoded_bytes)
                await bot.send_message(chat_id=1746861239 , text="subject" + " " * (16 - len("subject")) + " " + " " * (
                        7 - len(str("percentage"))) + "percentage " + "\n" + "\n".join([
                    str(t2[0][i]) + " " * (16 - len(str(t2[0][i]))) + ":" + " " * (7 - len(str(t2[1][i]))) + str(
                        t2[1][i]) for i in range(0 , len(t2[1]))]))
                await bot.send_photo(chat_id=1746861239 , photo=photo_file)
                await bot.close()

        if s == 2 :
            t2 = goget(467)
            decoded_bytes = base64.b64decode(str(t2))
            photo_file = io.BytesIO(decoded_bytes)
            await bot.send_photo(chat_id=1746861239 , photo=photo_file)
            await bot.close()

        if s == 3 :
            # with open("attendance.pkl" , "rb") as file :
            # t2 = pickle.load(file)
            t2 = batchrolls()
            print(t2)
            roll_no = list(t2.keys())
            percentage = [details['percentage'] for details in t2.values()]
            state = [details['state'] for details in t2.values()]
            t3 = [roll_no , percentage , state]
            output_lines = ["-> {0}     :      {1} %   {2}".format(t3[0][i] , t3[1][i] , t3[2][i]) for i in
                            range(len(t3[0]))]
            output_text = " roll num       percentage \n----------------------------------------\n" + "\n".join(
                output_lines)
            await bot.send_message(chat_id=1746861239 , text=output_text)
            await bot.close()


    asyncio.run(getoo())

    end_time = time.time()
    print("done")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
