import json
import requests
import random
import string
import zendriver as zd
import asyncio
from country_values import *


class Number:
    def __init__(self, id, number):
        self.id = id
        self.number = number

def generateName():
    base_url = "https://randomuser.me/api/"
    response = requests.get(f"{base_url}")
    if response.status_code == 200:
        data = response.json()
        person = data["results"][0]
        firstName = person["name"]["first"]
        lastName = person["name"]["last"]
        gender = person["gender"]
    return firstName, lastName, gender



def generateEmail(firstName, lastName, count):
    count += 1
    lastName_noSpaces = lastName.replace(" ", "")
    return firstName + '.' + lastName_noSpaces + str(random.randint(100, 999)) + f'{count}'


def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = ".,!?;:-_"

    # Make sure to include at least one from each group
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(punctuation),
    ]


    all_chars = lowercase + uppercase + digits + punctuation
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)
    return ''.join(password)

def generate_session_string(length=8):

    characters = string.ascii_letters + '123456789'  # Excludes '0'
    return ''.join(random.choices(characters, k=length))    


async def wait_for_url(tab, original_url, timeout=10):
    deadline = asyncio.get_event_loop().time() + timeout

    while True:
        result = await tab.send(zd.cdp.page.get_navigation_history())
        current_index = result[0]
        current_url = result[1][current_index].url

        if (current_url != original_url):
            return current_url
        
        if asyncio.get_event_loop().time() > deadline:
            raise TimeoutError("Timed out waiting for URL to change")
    
        await asyncio.sleep(0.1)




async def clear_cookies_except(tab, keep_domain):
    await tab.send(zd.cdp.network.enable())

    cookies_response = await tab.send(zd.cdp.network.get_all_cookies())
    all_cookies = cookies_response.get("cookies", [])

    for cookie in all_cookies:
        domain = cookie.get("domain", "").lstrip(".")
        if keep_domain not in domain:
            await tab.send(zd.cdp.network.delete_cookies(
                name=cookie["name"],
                domain=cookie["domain"],
                path=cookie["path"]
            ))

#asyncio.run(getPhoneNumber())













