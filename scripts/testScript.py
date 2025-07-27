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
from zendriver.cdp.network import Headers
from smsActivate import *
from smsProvider import *
from proxy import *
 

source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spoofed_offset_minutes = -180



#proxy_host = "geo.iproyal.com"
#proxy_port = 12321
#proxy_username = "KwkgoQ0MuFBREzYL"
#proxy = f"http://{proxy_host}:{proxy_port}"

#proxy_host = "isp.decodo.com"
#proxy_port = 10001

#proxy_username = 'user-spxcthqaa2-session-2t43lJ-country-de'
#proxy_password = 'Mz57jK9Wm=Mb4pattv'
#proxy = f"http://{proxy_host}:{proxy_port}"

#proxy_host = "v2.proxyempire.io"
#proxy_port = 5000
#proxy_username = "r_e05a824225-country-se-sid-f4df822"
#proxy_password = "118fb7879e"
#proxy = f"http://v2.proxyempire.io:5000"


#proxy = "la.residential.rayobyte.com:8000"
#proxy_username = "lorenzlanghammer7_gmail_com"
#proxy_password = "4R7rhACgPhG6udy-session-ajcd4f-country-it"

extension_path = os.path.join(source_dir, "extensions\WebRTC-Control")
extension_path = extension_path.replace("\\", "/")


def testPath():
    print(f"Resolved extension path: {extension_path}")
    print(f"Path exists: {os.path.exists(extension_path)}")
    print("Contents:", os.listdir(extension_path))

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



async def main():
    best_country = "usa"
    if (best_country):
        country = best_country.upper()
    proxyProvider = DecodoProxy(country)
    spoofed_timezone = CountryTimezone[country].value
    spoofed_language = Language[country].value
    hardware_concurrency = random.choice(hardware_concurrencies)
    device_memory = random.choice(device_memories)
    session_string = generate_session_string()

    
    #proxy_password = f"BMaEeNUjtiKcQZ8i_country-{CountryProxy[country].value}_session-{session_string}_lifetime-5m"

    #proxy_url = f"http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}"
    #proxies = {
    #    "http": proxy_url,
    #    "https": proxy_url,
    #}

    #ipify_response = requests.get("https://api.ipify.org?format=json", proxies=proxies, timeout=10)
    #ip = ipify_response.json()["ip"]
    #print(f"Public IP: {ip}")

    #ipinfo_response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=10)
    #timezone = ipinfo_response.json().get("timezone")
    #print(f"Timezone: {timezone}")

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
    source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    browser_dir = os.path.join(source_dir, "browser")
    browser = await zd.start(
        browser_args=[ 
            "--disable-extensions-except=" + extension_path,
            f"--load-extension={extension_path}",
            f"--proxy-server={proxyProvider.getProxy()}",
            f"--lang={spoofed_language}",

        ],     
                #user_data_dir=browser_dir,
                headless=False
    )

    tab = next(tab for tab in browser.targets if tab.type_ == "page")
    await tab.send(zd.cdp.page.enable())
    
    window_id, _ = await tab.send(zd.cdp.browser.get_window_for_target())
    await tab.send(zd.cdp.browser.set_window_bounds(
        window_id=window_id,
        bounds=Bounds(window_state=WindowState.MAXIMIZED)
    ))
    await tab.send(zd.cdp.emulation.set_timezone_override(timezone_id=spoofed_timezone))
    await tab.send(zd.cdp.page.add_script_to_evaluate_on_new_document(
        source=timezone_spoof_script
    ))

    with open("canvas_spoof.js", "r", encoding="utf-8") as f:
        canvas_spoof = f.read()

    await tab.send(zd.cdp.page.add_script_to_evaluate_on_new_document(
        source=canvas_spoof
    ))

    with open ("navigator_spoof.js", "r", encoding="utf-8") as f:
        navigator_spoof = f.read()
        navigator_spoof = navigator_spoof.format(hc=hardware_concurrency, dm=device_memory)

    await tab.send(zd.cdp.page.add_script_to_evaluate_on_new_document(
        source=navigator_spoof
    ))

    await tab.send(zd.cdp.network.enable())
    
    await tab.send(zd.cdp.network.set_extra_http_headers(
        headers=Headers({
            f"Accept-Language": CountryLanguageHeaders[country].value
        })
    ))

    await asyncio.sleep(3)
    #await tab.get("https://www.facebook.com/reg/")
    await tab.get("https://accounts.google.com/v3/signin/identifier?ifkv=AdBytiNUnbrmmJBaDpMjm4h7tj1LomWLQbHfBT9gDDKnqg-A4MS24DFPZxKj6PY7qJ1qrlYuTXM3Eg&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1927210506%3A1750601607868077")

    #await tab.send(zd.cdp.target.close_target(tab.target.target_id))
    
    
    enterCredentials_routine = EnterCredentials_routine(tab, proxyProvider.getUsername(), proxyProvider.getPassword())
    await enterCredentials_routine.executeRoutine()

    #selectAccountType_routine = SelectAccountType_routine(tab)
    #await selectAccountType_routine.executeRoutine()
    #await getNumber(tab)

    #await getNumber(browser)

    await asyncio.Event().wait()

asyncio.run(main())

#testPath()










