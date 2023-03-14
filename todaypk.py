from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pytz import timezone
from datetime import datetime
import time


def today():
    try:
        ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%d/%m/%Y')
        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=opt)
        driver.get("http://bit.ly/3Qb3MoX")
        driver.get("http://bit.ly/3Qb3MoX")
        driver.get("http://117.239.51.140/sitams/Academics/StudentAttendance.aspx?showtype=SA")
        driver.find_element(By.CSS_SELECTOR, '#radPeriod').click()
        driver.find_element(By.CSS_SELECTOR, '#txtFromDate').send_keys(ind_time)
        driver.find_element(By.CSS_SELECTOR, '#txtToDate').send_keys(ind_time)
        driver.find_element(By.CSS_SELECTOR, '#btnShow').click()
        tm = [driver.find_element(By.CSS_SELECTOR,
                                  f"#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child({i}) > td:nth-child(5)").text
              for i in range(2, 15)]
        total = driver.find_element(By.CSS_SELECTOR,
                                    "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(15) > td:nth-child(4)").text
        tm.append(total)
        driver.close()
        return tm


    except WebDriverException:
        return 'server not responding 404'


if __name__ == "__main__":
    start_time = time.time()
    t3 = today()
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(t3)
