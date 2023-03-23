import time
import asyncio
from pyppeteer import launch
from aiogram import *
import time
from PIL import Image
import io
import base64


#

async def goget(x):
    try:
        y = str(x)
        browser = await launch(executablePath='/usr/bin/google-chrome-stable', headless=True, args=['--no-sandbox'])
        page = await browser.newPage()
        await page.goto('http://bit.ly/3Qb3MoX')
        await page.goto('http://bit.ly/3Qb3MoX')
        await page.goto("http://117.239.51.140/sitams/Academics/StudentAttendance.aspx?")
        if len(y) == 2:
            await page.type('#txtRollNo', '20751A04' + y)
        elif 'l' in y:
            n = y.replace("l", "")
            await page.type('#txtRollNo', '21755A04' + n)
        elif 'l' not in y and len(y) == 3:
            await page.type('#txtRollNo', '20751A0' + y)
        await page.click('#radTillNow')
        await page.click('#btnShow')
        screenshot = await page.screenshot(fullPage=True)
        image = Image.open(io.BytesIO(screenshot)).convert('RGB')
        cropped_image = image.crop((10, 160, 760, 700))
        with io.BytesIO() as output:
            cropped_image.save(output, format='JPEG')
            image_bytes = output.getvalue()
        encoded_string = base64.b64encode(image_bytes).decode('utf-8')
        await browser.close()
        return encoded_string

    except:
        return "Nothing found"


async def date_attendance_67(ind_time):
    try:
        browser = await launch(executablePath='/usr/bin/google-chrome-stable', headless=True, args=['--no-sandbox'])
        page = await browser.newPage()
        await page.goto('http://bit.ly/3Qb3MoX')
        await page.goto('http://bit.ly/3Qb3MoX')
        await page.goto('http://117.239.51.140/sitams/Academics/StudentAttendance.aspx?showtype=SA')
        await page.click('#radPeriod')
        await page.type('#txtFromDate', ind_time)
        await page.type('#txtToDate', ind_time)
        await page.click('#btnShow')
        screenshot = await page.screenshot(fullPage=True)
        image = Image.open(io.BytesIO(screenshot)).convert('RGB')
        cropped_image = image.crop((10, 160, 760, 700))
        with io.BytesIO() as output:
            cropped_image.save(output, format='JPEG')
            image_bytes = output.getvalue()
        encoded_string = base64.b64encode(image_bytes).decode('utf-8')
        await browser.close()
        return encoded_string

    except:
        return "Nothing found"


async def date_attendance_32(ind_time):
    try:
        browser = await launch(executablePath='/usr/bin/google-chrome-stable', headless=True, args=['--no-sandbox'])
        page = await browser.newPage()
        await page.goto('http://bit.ly/3WUQsHy')
        await page.goto('http://bit.ly/3WUQsHy')
        await page.goto('http://117.239.51.140/sitams/Academics/StudentAttendance.aspx?showtype=SA')
        await page.click('#radPeriod')
        await page.type('#txtFromDate', ind_time)
        await page.type('#txtToDate', ind_time)
        await page.click('#btnShow')
        screenshot = await page.screenshot(fullPage=True)
        image = Image.open(io.BytesIO(screenshot)).convert('RGB')
        cropped_image = image.crop((10, 160, 760, 700))
        with io.BytesIO() as output:
            cropped_image.save(output, format='JPEG')
            image_bytes = output.getvalue()
        encoded_string = base64.b64encode(image_bytes).decode('utf-8')
        await browser.close()
        return encoded_string

    except:
        return "nothing found"


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


if __name__ == '__main__':
    start_time = time.time()


    async def no():
        encoded_string = await goget(232)
        decoded_bytes = base64.b64decode(str(encoded_string))
        photo_file = io.BytesIO(decoded_bytes)
        boto = Bot(token='6259883364:AAHdH_wd1-uaxD4EUw6kgBRbcM3MX40WUEw')
        await boto.send_photo(chat_id=1746861239, photo=photo_file)


    asyncio.get_event_loop().run_until_complete(no())
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")
