from gui_functions import *
from helper import *
import json
import os
from routine import *
from selenium import webdriver
import asyncio
import zendriver as zd
from zendriver.cdp.browser import Bounds, WindowState
from country_values import *
from fiveSim import *
from font_spoof import *
from zendriver.cdp.network import Headers
import pygetwindow as gw
import pyautogui as pag



source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
browser_dir = os.path.join(source_dir, "browser")
smsActivate_tab = None
emailname = "lorenzlanghammer7"
email_provider = "gmail.com"
password = "tHzf?j2hDi2G-QT"

async def getNumber(browser, initial_tab):
    '''
    browser = await zd.start(
        browser_args=[ 
            '--disable-webgl',
        ],     
        user_data_dir=browser_dir,
        headless=False
    )
    '''

    sms_tab = await browser.get("https://sms-activate.io/", new_tab=True)
    await sms_tab.send(zd.cdp.network.enable())    
    await asyncio.sleep(3)
    pag.press("ESC")
    #login_position = await get_position_by_selector("#newHeader > div.newHeader__bottom > div.newHeader__container > div > div.newHeader__controls > div.newHeader__user.user > div.user__setting > div > button.secondary-btn", sms_tab)
    
    '''
    moveToPoint(1611, 160, 2)
    pag.click()

    #email_position = await get_position_by_selector("#email", sms_tab)
    moveToPoint(852, 468, 2)
    pag.click()
    type(emailname)

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('alt')
    pyautogui.press('q')  
    pyautogui.keyUp('alt')
    pyautogui.keyUp('ctrl')

    type(email_provider)


    #password_position = await get_position_by_selector("#password", sms_tab)
    moveToPoint(879, 549, 2)
    pag.click()
    type(password)

    pag.press("Enter")
    '''



    google_position = await get_position_by_text("Google,youtube,Gmail", sms_tab)
    moveToPoint(google_position.x, google_position.y, 2)
    pag.click()
    await asyncio.sleep(3)

    find_country_position = await get_position_by_selector("#newLeft > div > div.newAside > div.activation-aside-tab > div.newAside-services-wrapper > div.newAside__services-wrapper > div > div.choice-service__wrapper > div > div.service-card.isActive > div.service-card__body > div.service-card__top-wrapper > div.service-card__search > div", sms_tab)
    moveToPoint(find_country_position.x, find_country_position.y, 2)
    pag.click()
    type("poland")
    await asyncio.sleep(3)

    scrollDown(2)


    buy_country_position = await get_position_by_selector("#newLeft > div > div.newAside > div.activation-aside-tab > div.newAside-services-wrapper > div.newAside__services-wrapper > div > div.choice-service__wrapper > div > div.service-card.isActive > div.service-card__body > div.service-card__country-wrapper > div > div > div > div.country-item__buy > div.country-item__buy-control > div.country-item__buy-basket > button", sms_tab)
    moveToPoint(buy_country_position.x - 50, buy_country_position.y, 2)
    pag.click()
    await asyncio.sleep(3)


    buy_position = await get_position_by_text("buy_country_position", sms_tab)
    moveToPoint(1100, 905, 2)
    pag.click()
    await asyncio.sleep(8)

    #number_element = await tab.select("#activationContainer_3761331902 > div.activate-grid-item__numberq > b", timeout=5)
    number_element = await sms_tab.find_element_by_text("+48", best_match=True)
    number = number_element.text_all
    print("found number")


    return number


async def getCode(initial_tab):

    chrome_windows = gw.getWindowsWithTitle('Chrome')
    sms_activate_title = "activat"
    for window in chrome_windows:
        print (window.title)
        if sms_activate_title.lower() in window.title.lower():
            try:
                window.restore()
                window.activate()
                window.maximize()
                break
            except Exception as e:
                print(f"Could not activate window: {e}")

    found_code = False
    global smsActivate_tab
    tab = smsActivate_tab
    tab.activate()
    
    while not found_code:
        code_element = await tab.select('[id^="activationContainer_"] span', timeout=5000)
        code = code_element.text_all
        if code == "Waiting SMS":
            print("code not found")
            continue
        else:
            print(code)
            found_code = True
    
    chrome_windows = gw.getWindowsWithTitle('Chrome')
    expected_title_keyword="Kod"

    for window in chrome_windows:
        #print (window.title)
        print("window found")
        if expected_title_keyword.lower() in window.title.lower():
            try:
                window.restore()
                window.activate()
                window.maximize()
                break
            except Exception as e:
                print(f"Could not activate window: {e}")
    
    await initial_tab.activate()

    return code



#asyncio.run(getNumber())
async def startBrowser():
    browser = await zd.start(
        browser_args=[ 
            '--disable-webgl',
        ],     
        user_data_dir=browser_dir,
        headless=False
    )


    tab = next(tab for tab in browser.targets if tab.type_ == "page")
    await tab.send(zd.cdp.page.enable())
    window_id, _ = await tab.send(zd.cdp.browser.get_window_for_target())
    await tab.send(zd.cdp.browser.set_window_bounds(
        window_id=window_id,
        bounds=Bounds(window_state=WindowState.MAXIMIZED)
    ))

    await asyncio.Event().wait()

#asyncio.run(getNumber())





