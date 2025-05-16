
from gui_functions import *
from helper import *
import json
import os
from routine import *
from selenium import webdriver
import asyncio
from playwright.async_api import async_playwright
import zendriver as zd
from zendriver.cdp.browser import Bounds, WindowState
from requests.auth import HTTPProxyAuth
import base64


month_days = {
    "January": 31,
    "February": 28, 
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

month_positions = {
     "January": 515,
    "February": 545,
    "March": 575,
    "April": 600,
    "May": 630,
    "June": 660,
    "July": 689,
    "August": 715,
    "September": 744,
    "October": 772,
    "November": 800,
    "December":829
}

async def main():
    browser = await zd.start(
        headless=False,
        launch_args=["--remote-debugging-port=9222"]
    )
    #tab = await browser.get("https://www.google.com")
    tab = await browser.get("https://accounts.google.com/v3/signin/identifier?ifkv=ASKV5MiaIcv1tYHTdF847w4aboMgloZwN_K9eUZEfmfgZNXL7PaNoEiX1ewJt8JSfInVpRjwNIcWXA&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S488045806%3A1747139268767111")
    window_id, _ = await tab.send(zd.cdp.browser.get_window_for_target())
    
    await tab.send(zd.cdp.browser.set_window_bounds(
        window_id=window_id,
        bounds=Bounds(window_state=WindowState.MAXIMIZED)
    ))

    await tab.send(zd.cdp.network.set_extra_http_headers())

    #searchPage_routine = SearchPage_routine(tab)
    #gotoPage_routine = GotoPage_routine(tab)

    #await searchPage_routine.executeRoutine()
    #await gotoPage_routine.executeRoutine()
    
    #await asyncio.sleep(1)

    #new_tab = browser.tabs[-1]
    #await new_tab.activate()

    selectAccountType_routine = SelectAccountType_routine(tab)
    await selectAccountType_routine.executeRoutine()

    enterName_routine = EnterName_routine(tab)
    await enterName_routine.executeRoutine()

    enterDateAndGender_routine = EnterDateAndGender_routine(tab)
    await enterDateAndGender_routine.executeRoutine()

    selectAddressType_routine = SelectAddressType_routine(tab)
    await selectAddressType_routine.executeRoutine()

    selectAddress_routine = SelectAddress_routine(tab)
    await selectAddress_routine.executeRoutine()

    enterPassword_routine = EnterPassword_routine(tab)
    await enterPassword_routine.executeRoutine()

    await asyncio.Event().wait()  # Wait forever

async def start_browser():
    proxy_host = "geo.iproyal.com"
    proxy_port = 12321
  
    # Launch browser with proxy
    browser = await zd.start(
        headless=False,
        args=[f"--proxy-server=http://{proxy_host}:{proxy_port}"]
    )
    tab = await browser.get()
    
    window_id, _ = await tab.send(zd.cdp.browser.get_window_for_target())
    await tab.send(zd.cdp.browser.set_window_bounds(
        window_id=window_id,
        bounds=Bounds(window_state=WindowState.MAXIMIZED)
    ))

    await tab.send(zd.cdp.network.enable())
    await asyncio.Event().wait()  # Wait forever

#asyncio.run(main())
asyncio.run(start_browser())

source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''
routines = [SearchPage_routine(), 
        GotoPage_routine(), 
        SelectAccountType_routine(),
        EnterName_routine(), 
        EnterDateAndGender_routine(), 
        SelectAddressType_routine(), 
        SelectAddress_routine()
        ]
'''

