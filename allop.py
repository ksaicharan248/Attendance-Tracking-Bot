import json
import threading
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


def altho():
    try:
        subjects, results = [], []
        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=opt)
        driver.set_window_size(1024, 768)
        driver.get("http://bit.ly/3Qb3MoX")
        driver.get("http://bit.ly/3Qb3MoX")
        driver.get("http://117.239.51.140/sitams/Academics/StudentAttendance.aspx?showtype=20751A0467")
        driver.find_element(By.CSS_SELECTOR, '#radTillNow').click()
        driver.find_element(By.CSS_SELECTOR, '#btnShow').click()
        for i in range(2, 15):
            selectors = [
                "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child({}) > td:nth-child({})".format(
                    i, col) for col in [2, 5]]
            values = [driver.find_element(By.CSS_SELECTOR, selector).text for selector in selectors]
            txt = [driver.find_element(By.CSS_SELECTOR,
                                       "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(15) > td:nth-child({})".format(
                                           i)).text for i in [1, 4]]
            subjects.append(values[0]), results.append(values[1])
        subjects.append(txt[0]), results.append(txt[1])
        driver.execute_script("document.body.style.fontFamily = 'Arial'") 
        screenshot = driver.get_screenshot_as_png()
        image = Image.open(io.BytesIO(screenshot)).convert('RGB')
        cropped_image = image.crop((10, 140, 970, 665))
        with io.BytesIO() as output:
            cropped_image.save(output, format='PNG', quality=10)
            image_bytes = output.getvalue()
        encoded_string = base64.b64encode(image_bytes).decode('utf-8')
        driver.close()
        return subjects, results, encoded_string

    except WebDriverException:
        return 'server not responding 404'


def altho_2():
    try:
        subjects, results = [], []
        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=opt)
        driver.set_window_size(1024, 768)
        driver.get("http://bit.ly/3WUQsHy")
        driver.get("http://bit.ly/3WUQsHy")
        driver.get("http://117.239.51.140/sitams/Academics/StudentAttendance.aspx?showtype=SA")
        driver.find_element(By.CSS_SELECTOR, '#radTillNow').click()
        driver.find_element(By.CSS_SELECTOR, '#btnShow').click()
        for i in range(2, 14):
            selectors = [
                "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child({}) > td:nth-child({})".format(
                    i, col) for col in [2, 5]]
            values = [driver.find_element(By.CSS_SELECTOR, selector).text for selector in selectors]
            txt = [driver.find_element(By.CSS_SELECTOR,
                                       "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(14) > td:nth-child({})".format(
                                           i)).text for i in [1, 4]]
            subjects.append(values[0]), results.append(values[1])
        subjects.append(txt[0]), results.append(txt[1])
        screenshot = driver.get_screenshot_as_png()
        image = Image.open(io.BytesIO(screenshot)).convert('RGB')
        cropped_image = image.crop((10, 140, 970, 650))
        with io.BytesIO() as output:
            cropped_image.save(output, format='JPEG')
            image_bytes = output.getvalue()
        encoded_string = base64.b64encode(image_bytes).decode('utf-8')
        driver.close()
        return subjects, results, encoded_string

    except WebDriverException:
        return 'server not responding 404'


def goget(x):
    try:
        y = str(x)
        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=opt)
        driver.set_window_size(1024, 768)
        driver.get("http://bit.ly/3Qb3MoX")
        driver.get("http://bit.ly/3Qb3MoX")
        driver.get("http://117.239.51.140/sitams/Academics/StudentAttendance.aspx?")
        if len(y) == 2:
            driver.find_element(By.CSS_SELECTOR, '#txtRollNo').send_keys("20751A04" + y)
        elif 'l' in y:
            n = y.replace("l", "")
            driver.find_element(By.CSS_SELECTOR, '#txtRollNo').send_keys("21755a04" + n)
        elif 'l' not in y and len(y) == 3:
            driver.find_element(By.CSS_SELECTOR, '#txtRollNo').send_keys("20751a0" + y)
        driver.find_element(By.CSS_SELECTOR, '#radTillNow').click()
        driver.find_element(By.CSS_SELECTOR, '#btnShow').click()
        screenshot = driver.get_screenshot_as_png()
        image = Image.open(io.BytesIO(screenshot)).convert('RGB')
        cropped_image = image.crop((10, 160, 970, 685))
        with io.BytesIO() as output:
            cropped_image.save(output, format='JPEG')
            image_bytes = output.getvalue()
        encoded_string = base64.b64encode(image_bytes).decode('utf-8')
        driver.close()
        return encoded_string

    except WebDriverException:
        return 'server not responding 404'


def batchroll():
    try:
        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=opt)
        driver.set_window_size(1024, 768)
        driver.get("http://bit.ly/3Qb3MoX")
        driver.get("http://bit.ly/3Qb3MoX")
        driver.get("http://117.239.51.140/sitams/Academics/StudentAttendance.aspx?")
        roll = [62, 64, 67, 69, 76, 86, 91, "A3", "A5"]
        attendance = []
        for i in range(0, len(roll)):
            driver.find_element(By.CSS_SELECTOR, '#txtRollNo').send_keys("20751A04" + str(roll[i]))
            driver.find_element(By.CSS_SELECTOR, '#radTillNow').click()
            driver.find_element(By.CSS_SELECTOR, '#btnShow').click()
            res = driver.find_element(By.CSS_SELECTOR,
                                      "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(15) > td:nth-child(4)").text
            attendance.append(res)
            driver.find_element(By.CSS_SELECTOR, '#txtRollNo').clear()
        data = list(zip(roll, attendance))
        data.sort(key=lambda x: x[1], reverse=True)
        roll_numbers = [x[0] for x in data]
        sorted_percentages = [x[1] for x in data]
        return roll_numbers, sorted_percentages


    except WebDriverException:

        return 'server not responding 404'


if __name__ == "__main__":
    start_time = time.time()


    async def getoo():
        bot = Bot(token='6259883364:AAHdH_wd1-uaxD4EUw6kgBRbcM3MX40WUEw')
        t3 =  altho()
        decoded_bytes = base64.b64decode(str(t3[2]))
        t3 = goget('67')
        decoded_bytes = base64.b64decode(str(t3))
        photo_file = io.BytesIO(decoded_bytes)
        await bot.send_photo(chat_id=1746861239, photo=photo_file)

    asyncio.run(getoo())
    end_time = time.time()
    print("done")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
