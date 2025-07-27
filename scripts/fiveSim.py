import json
import requests
import random
import string
import zendriver as zd
import asyncio
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


async def getPhoneNumber(country):

    url = f"https://5sim.net/v1/user/buy/activation/{country}/any/google?"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if(response.text == "no free phones"):
        return None

    country_upper = country.upper()
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


async def getCountry():

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
    
    return country


async def checkStatus(number_id):
    HEADERS = {
        'Authorization': f'Bearer {api_key}',
        'Accept': 'application/json'
    }

    url = f'https://5sim.net/v1/user/check/{number_id}'
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print("Error: ", response.text)
        return None

    data = response.json()
    status = data.get("status")
    
    if status == "RECEIVED":
        sms_list = data.get("sms", [])
        try:
            return sms_list[0].get("code", "")
        except:
            return None
    else:
        return None


async def cancelOrder(number_id):
    HEADERS = {
        'Authorization': f'Bearer {api_key}',
        'Accept': 'application/json'
    }

    url = 'https://5sim.net/v1/user/cancel/'
    response = requests.get(url + str(number_id), headers=HEADERS)
    data = response.json()
    status = data.get("status")
    print(status)
    if (status != "CANCELED"):
        print("order cancelled")
        return False
    else:
         print("could not cancel")
         return True 














