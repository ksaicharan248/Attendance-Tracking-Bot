from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pytz import timezone
from datetime import datetime


def today():
    ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%d/%m/%Y')
    opt = Options()
    opt.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=opt)
    driver.get("http://bit.ly/3Qb3MoX")
    driver.get("http://bit.ly/3Qb3MoX")
    # driver.find_element(By.CSS_SELECTOR, '#txtId2').send_keys("20751A0467")
    # driver.find_element(By.CSS_SELECTOR, '#txtPwd2').send_keys("Sai@#123")
    # driver.find_element(By.CSS_SELECTOR, '#imgBtn2').click()
    driver.get("http://117.239.51.140/sitams/Academics/StudentAttendance.aspx?showtype=SA")
    driver.find_element(By.CSS_SELECTOR, '#radPeriod').click()
    driver.find_element(By.CSS_SELECTOR, '#txtFromDate').send_keys(ind_time)
    driver.find_element(By.CSS_SELECTOR, '#txtToDate').send_keys(ind_time)
    driver.find_element(By.CSS_SELECTOR, '#btnShow').click()
    cs = driver.find_element(By.CSS_SELECTOR,"#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(2) > td:nth-child(5)").text
    EMTL = driver.find_element(By.CSS_SELECTOR, "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(3) > td:nth-child(5)").text
    vlsi= driver.find_element(By.CSS_SELECTOR, "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(4) > td:nth-child(5)").text
    emi= driver.find_element(By.CSS_SELECTOR, "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(5) > td:nth-child(5)").text
    irob= driver.find_element(By.CSS_SELECTOR, "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(6) > td:nth-child(5)").text
    map= driver.find_element(By.CSS_SELECTOR, "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(7) > td:nth-child(5)").text
    cslb= driver.find_element(By.CSS_SELECTOR, "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(8) > td:nth-child(5)").text
    vlsilb = driver.find_element(By.CSS_SELECTOR, "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(9) > td:nth-child(5)").text
    coi = driver.find_element(By.CSS_SELECTOR, "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(10) > td:nth-child(5)").text
    con= driver.find_element(By.CSS_SELECTOR, "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(11) > td:nth-child(5)").text
    lib= driver.find_element(By.CSS_SELECTOR, "#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(12) > td:nth-child(5)").text
    txt = driver.find_element(By.CSS_SELECTOR,"#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(13) > td:nth-child(4)").text
    driver.close()
    return cs, EMTL, vlsi, emi, irob, map, cslb, vlsilb, coi, con, lib, txt