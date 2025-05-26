import json
import requests
import random
import string
import requests
import zendriver as zd
import asyncio
from fivesim import FiveSim, Country, Operator, FiveSimError
from country_values import *

api_key = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzkzOTk2NzQsImlhdCI6MTc0Nzg2MzY3NCwicmF5IjoiMzZjNGUwM2U4MTIzYjExNTNmZjM4ZGU1ZDk3MzJiMTgiLCJzdWIiOjMxNzM3MzV9.EI5Vcv07CNIJk-pPAsc5V2-eT0u7nrXzcbuTmNtfkdf0p5ffmWqUvp8tf5IM-QVCC67e73ZaVnhYJxvu9Ze4qqsVNQLR_cyAFnblg9ody8FBDDtILZLaG68KE9nqKuj6Uz-oqzicCh36fVdBHHXFuFyPFcHoPv3h_-016kMFRPqtozoZ4w_0AAt8tzdO904ayi82c-KK0EbgAi_mEmacnok62SGAty_0UewC39qR3QWmDlKal4ClICqLn9bp7emPNDamdZ-HvD9-JEiqnSsXk2wYVMP1fEqBvhPLA16MiYxB0Nh0-80Fkb5ozE83uer6Rm1fYQuGAiYmTXkXsZCf-A"
rate_fields = ["rate", "rate1", "rate3", "rate24", "rate72", "rate168", "rate720"]

max_price = 50
min_success_rate = 10
target_service = "google"
country_list = [country.value for country in Country]

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
    return firstName + '.' + lastName + f'{count}'


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


async def getPhoneNumber():

    url = f"https://5sim.net/v1/guest/prices"
    response = requests.get(url)
    data = response.json()

    lowest_price = float('inf')
    best_offer = None

    for country_name, services in data.items():
        if country_name in country_list:
            for service, vendors in services.items():
                if (service == target_service):
                    for vendor, info in vendors.items():
                        cost = info.get('cost', float('inf'))
                        if cost <= max_price and info.get('count', 0) > 0:
                            if any(info.get(rate, 0) >= min_success_rate for rate in rate_fields):
                                if cost < lowest_price:
                                    lowest_price = cost
                                    best_offer = {
                                        "country": country_name,
                                        "vendor": vendor,
                                        "cost": cost,
                                        "info": info
                                    }

    print(best_offer)
    country = best_offer['country']
    operator = best_offer['vendor']
    price = best_offer['cost']
    


    url = f"https://5sim.net/v1/user/buy/activation/{country}/any/google?"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    print("Status:", response.status_code)
    print("Response:", response.text)

    country_upper = best_offer['country'].upper()
    country_code = CountryCode[country_upper].value

    try:
        fullResponse = response.json()
    except:
        return None
    
    phone = fullResponse['phone']
    id = fullResponse['id']

    try:
        country_code = CountryCode[country.upper()].value
        number = (phone[len(country_code):] if phone.startswith(country_code) else phone)
        return Number(id, number)
    except KeyError:
        print("could not format number")
        return None
 





#asyncio.run(getPhoneNumber())













