import zendriver as zd
from zendriver.cdp import fetch
import asyncio

proxy_host = "geo.iproyal.com"
proxy_port = 12321
proxy_username = "KwkgoQ0MuFBREzYL"
proxy_password = "BMaEeNUjtiKcQZ8i_country-de_city-aachen_session-akqS664V_lifetime-30m"
proxy = f"http://{proxy_host}:{proxy_port}"


async def setup_proxy(username, password, tab):
    async def auth_challenge_handler(event: fetch.AuthRequired):
        print("auth required")
        await tab.send(
            fetch.continue_with_auth(
                request_id=event.request_id,
                auth_challenge_response=fetch.AuthChallengeResponse(
                    response="ProvideCredentials",
                    username=username,
                    password=password
                ),
            )
        )

    async def req_paused(event: fetch.RequestPaused):
        await tab.send(fetch.continue_request(request_id=event.request_id))
    
    tab.add_handler(
        fetch.RequestPaused, lambda event: asyncio.create_task(req_paused(event))
    )

    tab.add_handler(
        fetch.AuthRequired,
        lambda event: asyncio.create_task(auth_challenge_handler(event)),
    )

    await tab.send(fetch.enable(handle_auth_requests=True))


async def start_browser():
    browser = await zd.start(browser_args=[f"--proxy-server={proxy}"])
    tabs = await browser.tabs()
    main_tab = tabs[0] if tabs else await browser.get("draft:,")

# Setup proxy interception BEFORE navigating anywhere
    await setup_proxy(proxy_username, proxy_password, main_tab)
    await main_tab.get("https://httpbin.org/ip")  # Or any IP check page

    await asyncio.Event().wait()  # Wait forever


asyncio.run(start_browser())
















