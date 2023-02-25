from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from PIL import Image
import io
import base64


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
        for i in range(2, 13):
            selectors = [
                "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child({}) > td:nth-child({})".format(
                    i, col) for col in [2, 5]]
            values = [driver.find_element(By.CSS_SELECTOR, selector).text for selector in selectors]
            txt = [driver.find_element(By.CSS_SELECTOR,
                                       "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(13) > td:nth-child({})".format(
                                           i)).text for i in [1, 4]]
            subjects.append(values[0]), results.append(values[1])
        subjects.append(txt[0]), results.append(txt[1])
        screenshot = driver.get_screenshot_as_png()
        image = Image.open(io.BytesIO(screenshot)).convert('RGB')
        cropped_image = image.crop((10, 140, 970, 620))
        with io.BytesIO() as output:
            cropped_image.save(output, format='PNG', quality=100)
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
        driver.get("http://117.239.51.140/sitams/Academics/StudentAttendance.aspx?showtype=20751A0232")
        driver.find_element(By.CSS_SELECTOR, '#radTillNow').click()
        driver.find_element(By.CSS_SELECTOR, '#btnShow').click()
        for i in range(2, 13):
            selectors = [
                "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child({}) > td:nth-child({})".format(
                    i, col) for col in [2, 5]]
            values = [driver.find_element(By.CSS_SELECTOR, selector).text for selector in selectors]
            txt = [driver.find_element(By.CSS_SELECTOR,
                                       "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(13) > td:nth-child({})".format(
                                           i)).text for i in [1, 4]]
            subjects.append(values[0]), results.append(values[1])
        subjects.append(txt[0]), results.append(txt[1])
        screenshot = driver.get_screenshot_as_png()
        image = Image.open(io.BytesIO(screenshot)).convert('RGB')
        cropped_image = image.crop((10, 140, 970, 620))
        with io.BytesIO() as output:
            cropped_image.save(output, format='JPEG')
            image_bytes = output.getvalue()
        encoded_string = base64.b64encode(image_bytes).decode('utf-8')
        driver.close()
        return subjects, results, encoded_string

    except WebDriverException:
        return 'server not responding 404'


if __name__ == "__main__":
    t2 = altho()
    print(t2)
