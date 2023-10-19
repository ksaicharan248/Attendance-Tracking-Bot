from aiogram import *
import asyncio
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from PIL import Image
import io
import base64


def today(ind_time):
    try:
        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=opt)
        driver.set_window_size(1024, 768)
        driver.get("http://bit.ly/3Qb3MoX")
        driver.get("http://bit.ly/3Qb3MoX")
        driver.get("http://117.239.51.140/sitams/Academics/StudentAttendance.aspx?showtype=SA")
        driver.find_element(By.CSS_SELECTOR, '#radPeriod').click()
        driver.find_element(By.CSS_SELECTOR, '#txtFromDate').send_keys(ind_time)
        driver.find_element(By.CSS_SELECTOR, '#txtToDate').send_keys(ind_time)
        driver.find_element(By.CSS_SELECTOR, '#btnShow').click()
        div_element = driver.find_element('css selector' , '#tblReport')
        driver.execute_script(
            f'document.querySelector("#tblReport").style.height ="{int(div_element.size["height"]) + 15}px";')
        screenshot = div_element.screenshot_as_png
        image = Image.open(io.BytesIO(screenshot)).convert('RGB')
        with io.BytesIO() as output :
            image.save(output , format='JPEG')
            image_bytes = output.getvalue()
        encoded_string = base64.b64encode(image_bytes).decode('utf-8')
        driver.close()
        return encoded_string


    except WebDriverException:
        return 'server not responding 404'


def today_rs(ind_time):
    try:
        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=opt)
        driver.set_window_size(1024, 768)
        driver.get("http://bit.ly/3WUQsHy")
        driver.get("http://bit.ly/3WUQsHy")
        driver.get("http://117.239.51.140/sitams/Academics/StudentAttendance.aspx?showtype=SA")
        driver.find_element(By.CSS_SELECTOR, '#radPeriod').click()
        driver.find_element(By.CSS_SELECTOR, '#txtFromDate').send_keys(ind_time)
        driver.find_element(By.CSS_SELECTOR, '#txtToDate').send_keys(ind_time)
        driver.find_element(By.CSS_SELECTOR, '#btnShow').click()
        div_element = driver.find_element('css selector' , '#tblReport')
        driver.execute_script(
            f'document.querySelector("#tblReport").style.height ="{int(div_element.size["height"]) + 15}px";')
        screenshot = div_element.screenshot_as_png
        image = Image.open(io.BytesIO(screenshot)).convert('RGB')
        with io.BytesIO() as output :
            image.save(output , format='JPEG')
            image_bytes = output.getvalue()
        encoded_string = base64.b64encode(image_bytes).decode('utf-8')
        driver.close()
        return encoded_string


    except WebDriverException:
        return 'server not responding 404'


def dato(s=""):
    if "-" in s:
        s = s.replace("-", "/")
    ob = time.gmtime(time.time())
    if s == "":
        m = str(ob[2]) + '/' + str(ob[1]) + '/' + str(ob[0])
    elif len(s) <= 2 and '/' not in s:
        m = s + '/' + str(ob[1]) + '/' + str(ob[0])

    elif '/' in s and len(s) <= 5:
        m = s + '/' + str(ob[0])

    else:
        m = s
    return m


if __name__ == "__main__":
    start_time = time.time()
    async def getoo():
        bot = Bot(token='6259883364:AAHdH_wd1-uaxD4EUw6kgBRbcM3MX40WUEw')
        date = dato("")
        t3 = today(date)
        decoded_bytes = base64.b64decode(str(t3))
        photo_file = io.BytesIO(decoded_bytes)
        await bot.send_photo(chat_id=1746861239, photo=photo_file)
    asyncio.run(getoo())
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")

