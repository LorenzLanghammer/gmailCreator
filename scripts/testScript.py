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

extension_path = os.path.join(source_dir, "extensions\WebRTC-Control")
extension_path = extension_path.replace("\\", "/")


def testPath():
    print(f"Resolved extension path: {extension_path}")
    print(f"Path exists: {os.path.exists(extension_path)}")
    print("Contents:", os.listdir(extension_path))


async def main():
    best_country = "england"
    if (best_country):
        country = best_country.upper()
    spoofed_timezone = CountryTimezone[country].value
    spoofed_language = Language[country].value
    
    proxy_password = f"BMaEeNUjtiKcQZ8i_country-gb_session-4Gf6kcB_lifetime-30m"

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
            f"--load-extension={extension_path}",
            "--auto-open-devtools-for-tabs",
            f"--proxy-server={proxy}",
            f"--lang={spoofed_language}",



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
    await tab.get("https://google.com")

    enterCredentials_routine = EnterCredentials_routine(tab, proxy_username, proxy_password)
    await enterCredentials_routine.executeRoutine()

    await asyncio.Event().wait()

asyncio.run(main())

#testPath()
