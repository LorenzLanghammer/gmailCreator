
import sys
import os
from fb_routines import *


script_dir = os.path.dirname(os.path.abspath(__file__))        
scripts_dir = os.path.abspath(os.path.join(script_dir, "..", "scripts"))  
sys.path.append(scripts_dir)

print("scripts_dir added to sys.path:", scripts_dir)

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
from smsActivate import *
from font_spoof import *
from zendriver.cdp.network import Headers
from proxy import * 
import multiprocessing


hardware_concurrencies = [
    4,
    8,
    6,
    12,
    16
]

device_memories = [
    4,
    8
]


source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


best_country = "germany"

extension_path_rtc = os.path.join(source_dir, "extensions/WebRTC-Control")
extension_path_canvas = os.path.join(source_dir, "extensions/canvas_fingerprint_defender")
if (best_country):
        country = best_country.upper()
proxyProvider = DecodoProxy(country)
spoofed_offset_minutes = TimeOffset[country].value


async def main():
    name = generateName()
    username = generateEmail(name[0], name[1], 2)
    spoofed_timezone = CountryTimezone[country].value
    spoofed_language = Language[country].value
    session_string = generate_session_string()
    hardware_concurrency = random.choice(hardware_concurrencies)
    device_memory = random.choice(device_memories)
    source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    browser = await zd.start(
        browser_args=[ 
            "--disable-extensions-except=" + extension_path_rtc,
            f"--lang={spoofed_language}",
            f"--proxy-server={proxyProvider.getProxy()}",
            f"--load-extension={extension_path_rtc}, {extension_path_canvas}",
            '--disable-webgl',
        ],     
        headless=False,
        no_sandbox=True
    )


    initial_tab = next(tab for tab in browser.targets if tab.type_ == "page")
    await initial_tab.send(zd.cdp.page.enable())

    with open (os.path.join(scripts_dir, "navigator_spoof.js"), "r", encoding="utf-8") as f:
        navigator_spoof = f.read()
        navigator_spoof = navigator_spoof.format(hc=hardware_concurrency, dm=device_memory)

    await initial_tab.send(zd.cdp.page.add_script_to_evaluate_on_new_document(
        source=navigator_spoof
    ))

    with open(os.path.join(scripts_dir, "timezone_spoof.js"), "r", encoding="utf-8") as f:
        timezone_spoof = f.read()
        timezone_spoof = timezone_spoof.format(spoofed_timezone=spoofed_timezone, spoofed_offset_minutes=spoofed_offset_minutes)
    
    await initial_tab.send(zd.cdp.page.add_script_to_evaluate_on_new_document(
        source=timezone_spoof
    ))

    with open(os.path.join(scripts_dir, "canvas_spoof.js"), "r", encoding="utf-8") as f:
        canvas_spoof = f.read()

    await initial_tab.send(zd.cdp.page.add_script_to_evaluate_on_new_document(
        source=canvas_spoof
    ))

    await initial_tab.send(zd.cdp.network.set_extra_http_headers(
        headers=Headers({
            f"Accept-Language": CountryLanguageHeaders[country].value
        })
    ))
    


    window_id, _ = await initial_tab.send(zd.cdp.browser.get_window_for_target())

    await initial_tab.send(zd.cdp.browser.set_window_bounds(
        window_id=window_id,
        bounds=Bounds(window_state=WindowState.MAXIMIZED)
    ))
    
    
    await initial_tab.send(zd.cdp.emulation.set_timezone_override(timezone_id=spoofed_timezone))
   

    await asyncio.sleep(3)
    await initial_tab.get("https://myaccount.google.com/apppasswords")
    enterCredentials_routine = EnterCredentials_routine(initial_tab, proxyProvider.getUsername(), proxyProvider.getPassword())
    await enterCredentials_routine.executeRoutine()

    #acceptCookies_routine = AcceptCookiesRoutine(initial_tab)
    #await acceptCookies_routine.executeRoutine()

    enter_position = await get_position_by_selector("#yDmH0d > c-wiz > div > div:nth-child(2) > div:nth-child(2) > c-wiz > div > div.VfPpkd-WsjYwc.VfPpkd-WsjYwc-OWXEXe-INsAgc.KC1dQ.Usd1Ac.AaN0Dd.F2KCCe.NkyfNe.HYI7Re.yOXhRb.hG48Q > div > div:nth-child(4) > div > div:nth-child(2) > div > div > label > span.VfPpkd-fmcmS-OyKIhb", initial_tab)
    moveToPoint(enter_position.x, enter_position.y, 2)
    pag.click()
    type("imapScript")

    create_position = await get_position_by_selector("#yDmH0d > c-wiz > div > div:nth-child(2) > div:nth-child(2) > c-wiz > div > div.VfPpkd-WsjYwc.VfPpkd-WsjYwc-OWXEXe-INsAgc.KC1dQ.Usd1Ac.AaN0Dd.F2KCCe.NkyfNe.HYI7Re.yOXhRb.hG48Q > div > div:nth-child(4) > div > div.KL6Gkf.lY6Rwe > div > div > div > button > span.AeBiU-RLmnJb", initial_tab)
    moveToPoint(create_gmail_position.x, create_gmail_position.y, 2)
    pag.click()

    moveToPoint(839, 475, 2)
    pyautogui.mouseDown()
    moveToPoint(1084, 475, 2)
    pag.mouseUp()
    pyautogui.hotkey('ctrl', 'c')
    copied_text = pyperclip.paste()

    print(copied_text)


    '''
    
    '''





def run_main():
    asyncio.run(main())

if __name__ == "__main__":
    while True:
        p = multiprocessing.Process(target=run_main)
        p.start()
        p.join()
        print("Browser closed. Restarting...")








