import asyncio
import time
import pyppeteer
from pyppeteer import launch
import timeit
import datetime
from datetime import datetime, timedelta, timezone


def attandence():
    loop = asyncio.new_event_loop()
    tz = timezone(timedelta(hours=5, minutes=30))
    ind_time = datetime.now(tz).strftime('%d/%m/%Y')
    asyncio.set_event_loop(loop)
    browser = loop.run_until_complete(launch(headless=True))
    page = loop.run_until_complete(browser.newPage())
    loop.run_until_complete(page.goto("http://bit.ly/3Qb3MoX"))
    loop.run_until_complete(page.goto("http://bit.ly/3Qb3MoX"))
    loop.run_until_complete(page.goto("http://117.239.51.140/sitams/Academics/StudentAttendance.aspx?showtype=SA"))
    loop.run_until_complete(page.click('#radPeriod'))
    loop.run_until_complete(page.type('#txtFromDate', ind_time))
    loop.run_until_complete(page.type('#txtToDate', ind_time))
    loop.run_until_complete(page.click('#btnShow'))
    cs = loop.run_until_complete(page.evaluate(
        'document.querySelector("#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(2) > td:nth-child(5)").textContent'))
    EMTL = loop.run_until_complete(page.evaluate(
        'document.querySelector("#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(3) > td:nth-child(5)").textContent'))
    vlsi = loop.run_until_complete(page.evaluate(
        'document.querySelector("#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(4) > td:nth-child(5)").textContent'))
    emi = loop.run_until_complete(page.evaluate(
        'document.querySelector("#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(5) > td:nth-child(5)").textContent'))
    irob = loop.run_until_complete(page.evaluate(
        'document.querySelector("#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(6) > td:nth-child(5)").textContent'))
    map = loop.run_until_complete(page.evaluate(
        'document.querySelector("#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(7) > td:nth-child(5)").textContent'))
    cslab = loop.run_until_complete(page.evaluate(
        'document.querySelector("#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(8) > td:nth-child(5)").textContent'))
    vlsilb = loop.run_until_complete(page.evaluate(
        'document.querySelector("#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(9) > td:nth-child(5)").textContent'))
    coi = loop.run_until_complete(page.evaluate(
        'document.querySelector("#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(10) > td:nth-child(5)").textContent'))
    con = loop.run_until_complete(page.evaluate(
        'document.querySelector("#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(11) > td:nth-child(5)").textContent'))
    lib = loop.run_until_complete(page.evaluate(
        'document.querySelector("#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(12) > td:nth-child(5)").textContent'))
    txt = loop.run_until_complete(page.evaluate(
        'document.querySelector("#tblReport > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(13) > td:nth-child(4)").textContent'))
    loop.run_until_complete(browser.close())
    return cs, EMTL, vlsi, emi, irob, map, cslab, vlsilb, coi, con, lib, txt


if __name__ == "__main__":
    start_time = time.time() 
    result = attandence()
    print(result)
    end_time = time.time()  

    time_taken = end_time - start_time 

    print(f"start Time taken: {start_time:.2f} seconds")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"end Time taken: {end_time:.2f} seconds")
