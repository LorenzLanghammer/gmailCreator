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
spoofed_offset_minutes = -120


proxy_host = "geo.iproyal.com"
proxy_port = 12321
proxy_username = "KwkgoQ0MuFBREzYL"
proxy = f"http://{proxy_host}:{proxy_port}"

extension_path = os.path.join(source_dir, "extensions/WebRTC-Control")

async def main():
    best_country = "england"
    if (best_country):
        country = best_country.upper()
    spoofed_timezone = CountryTimezone[country].value
    spoofed_language = Language[country].value
    session_string = generate_session_string()
    proxy_password = f"BMaEeNUjtiKcQZ8i_country-gb_session-{session_string}_lifetime-5m"

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
            "--disable-extensions-except=" + extension_path,
            f"--lang={spoofed_language}",
            f"--proxy-server={proxy}",
            f"--load-extension={extension_path}",
            '--disable-webgl',
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


    await asyncio.sleep(3)
    await tab.get("https://accounts.google.com/v3/signin/identifier?ifkv=AdBytiNHx9gqOjAdI2ImvqBApnsU4v_SN9dVm1yaJibrHqQTWdBo6pWrMnKSzgnZU8HYlBGaR53q&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S471759149%3A1748625151149630")
    #await tab.get("https://google.com")
    
    enterCredentials_routine = EnterCredentials_routine(tab, proxy_username, proxy_password)
    await enterCredentials_routine.executeRoutine()

    '''
    searchPage_routine = SearchPage_routine(tab)
    await searchPage_routine.executeRoutine()

    gotoPage_routine = GotoPage_routine(tab)
    await gotoPage_routine.executeRoutine()
    
    await asyncio.sleep(1)

    new_tab = browser.tabs[-1]
    await new_tab.activate()
    await asyncio.Event().wait()  
    '''

    

    routines = [ 
        SelectAccountType_routine(tab),
        EnterName_routine(tab), 
        EnterDateAndGender_routine(tab), 
        SelectAddressType_routine(tab), 
        SelectAddress_routine(tab),
        EnterPassword_routine(tab),
        EnterPhoneNumber_routine(tab, best_country),
        DeclineRecoveryMailRoutine(tab)
        ]

    await asyncio.sleep(2)

    # Send the command
    result = await tab.send(zd.cdp.page.get_navigation_history())

    print(result)

    while True:
        for routine in routines:
            if routine.identifier in current_url:
                await routine.executeRoutine()
                current_url = await tab.get_all_urls()
                continue
        break
        

    await asyncio.Event().wait()  


asyncio.run(main())


'''
if (current_url.includes(selectAccountType_routine.identifier)):
            await selectAccountType_routine.executeRoutine()
            print("identifer of selectAccountType routine found")
            continue
        if (await is_element_on_page(enterName_routine.identifier, tab)):
            await enterName_routine.executeRoutine()
            continue
        if (await is_element_on_page(enterDateAndGender_routine.identifier, tab)):
            await enterDateAndGender_routine.executeRoutine()
            continue
        if (await is_element_on_page(selectAddressType_routine.identifier, tab)):
            await selectAddressType_routine.executeRoutine()
            continue
        if (await is_element_on_page(selectAddress_routine.identifier,tab)):
            await selectAddress_routine.executeRoutine()
            continue
        if (await is_element_on_page(enterPassword_routine.identifier, tab)):
            await enterPassword_routine.executeRoutine()
            continue
        if (await is_element_on_page(enterPhoneNumber_routine.identifier, tab)):
            await enterPhoneNumber_routine.executeRoutine()
            continue
        if (await is_element_on_page(declineRecoveryMail_routine.identifier, tab)):
            await declineRecoveryMail_routine.executeRoutine()
            continue
        break

'''






