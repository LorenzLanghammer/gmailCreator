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


source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spoofed_timezone = "Europe/London"
spoofed_offset_minutes = -120


proxy_host = "geo.iproyal.com"
proxy_port = 12321
proxy_username = "KwkgoQ0MuFBREzYL"
proxy_password = "BMaEeNUjtiKcQZ8i_country-gb_session-9TAfasdfN1_lifetime-30m"
proxy = f"http://{proxy_host}:{proxy_port}"
extension_path = os.path.join(source_dir, "extensions/WebRTC-Control")

async def main():

    country = getCountry().upper()
    spoofed_timezone = CountryCode[country].value
    spoofed_language = Language[country].value

    timezone_spoof_script = f"""
        (() => {{
            const spoofedTimeZone = {spoofed_timezone};
            const originalResolvedOptions = Intl.DateTimeFormat.prototype.resolvedOptions;
            Intl.DateTimeFormat.prototype.resolvedOptions = function() {{
                const options = originalResolvedOptions.apply(this, arguments);
                options.timeZone = spoofedTimeZone;
                return options;
            }};

            const originalGetTimezoneOffset = Date.prototype.getTimezoneOffset;
            Date.prototype.getTimezoneOffset = function() {{
                return {spoofed_offset_minutes};
            }};

            const offsetMs = {spoofed_offset_minutes} * 60 * 1000;
            const OriginalDate = Date;
            function FakeDate(...args) {{
                if (args.length === 0) {{
                    return new OriginalDate(OriginalDate.now() - offsetMs);
                }}
                return new OriginalDate(...args);
            }}
            FakeDate.UTC = OriginalDate.UTC;
            FakeDate.now = () => OriginalDate.now() - offsetMs;
            FakeDate.parse = OriginalDate.parse;
            FakeDate.prototype = OriginalDate.prototype;
            window.Date = FakeDate;
        }})();
        """

    browser = await zd.start(
        browser_args=[ 
            f"--lang={spoofed_language}",
            f"--proxy-server={proxy}",
            f"--load-extension={extension_path}",
            '--disable-webgl',
            '--disable-3d-apis',
        ],     
                headless=False
    )

    tab = await browser.get()
    window_id, _ = await tab.send(zd.cdp.browser.get_window_for_target())
    await tab.send(zd.cdp.browser.set_window_bounds(
        window_id=window_id,
        bounds=Bounds(window_state=WindowState.MAXIMIZED)
    ))
    await tab.send(zd.cdp.emulation.set_timezone_override(timezone_id=spoofed_timezone))
    await tab.send(zd.cdp.page.add_script_to_evaluate_on_new_document(
        source=timezone_spoof_script
    ))


    asyncio.sleep(3)
    await tab.get("https://google.com")

    enterCredentials_routine = EnterCredentials_routine(tab, proxy_username, proxy_password)
    await enterCredentials_routine.executeRoutine()

    await asyncio.Event().wait()  # Wait forever


'''
    searchPage_routine = SearchPage_routine(tab)
    await searchPage_routine.executeRoutine()

    gotoPage_routine = GotoPage_routine(tab)
    await gotoPage_routine.executeRoutine()
    
    await asyncio.sleep(1)

    new_tab = browser.tabs[-1]
    await new_tab.activate()
    await asyncio.Event().wait()  # Wait forever


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
'''


async def start_browser():
    proxy_host = "geo.iproyal.com"
    proxy_port = 12321

    proxy = f"http://{proxy_host}:{proxy_port}"

    browser = await zd.start(browser_args=[f"--proxy-server={proxy}"])
    main_tab = await browser.get()
    await asyncio.Event().wait()  # Wait forever

asyncio.run(main())

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


