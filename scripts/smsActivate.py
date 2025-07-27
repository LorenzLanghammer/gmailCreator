import json
import requests
import random
import string
import zendriver as zd
import asyncio
from country_values import *
from smsactivate.api import SMSActivateAPI
import pyautogui
import pyperclip



api_key = "8318bf02e3cf43fA9727fe18d21063bc"
rate_fields = ["rate", "rate1", "rate3", "rate24", "rate72", "rate168", "rate720"]
sa = SMSActivateAPI(api_key)


max_price = 50
min_success_rate = 10
target_service = "google"
country_list = [country.value for country in Country]

class Number:
    def __init__(self, id, number):
        self.id = id
        self.number = number



async def getPhoneNumber(country):
    request_params = {  'api_key': api_key, 
                        'action': 'getNumber',
                        'service': 'go', 
                        'country': CountryNumber[country].value, 
                        'operator': 'any'
                        }
    response = requests.get(f"https://sms-activate.org/stubs/handler_api.php", params=request_params)
    if response.status_code == 200:
        parts = response.text.split(':')
        if parts[0] == 'ACCESS_NUMBER':
            activation_id = parts[1]
            phone_number = parts[2]
            return Number(id=activation_id, number=phone_number)
        else:
            print("Error: ", response.text)
            return None
    else:
        print("Http error: ", response.status_code)
        return None



async def getCountry():
    return


async def checkStatus(number_id):
    def get_status():
        return sa.getStatus(id=number_id)
    
    status = await asyncio.to_thread(get_status)
    
    if status.startswith("STATUS_OK:"):
        return status.split(":")[1]
    
    elif status == "STATUS_WAIT_CODE":
        print("Status:", status)
        return None

async def cancelOrder(number_id):
    return


def test(country):

    SERVICE = 'go'  
    country_id = CountryNumber[country].value
    

    request_params = {  'api_key': api_key, 
                            'action': 'getNumbersStatus',
                            'service': 'go', 
                            'country': country_id, 
                            'operator': 'any',
                            'freePrice': True
                            }

    url = 'https://api.sms-activate.org/stubs/handler_api.php'
    response = requests.get(url, params=request_params)

    try:
        data = response.json()
        if SERVICE in data:
            print(f"Available numbers for {SERVICE.upper()} in country {country_id}: {data[SERVICE]}")
        else:
            print(f"No data available for service '{SERVICE}'. Full response:\n{data}")
    except Exception as e:
        print("Failed to parse JSON response:", e)


def getNumberOfNumbers():
    countries = ["ISRAEL"]
    for country in countries:
        test(country)
   

import pyotp

# Your TOTP secret (no spaces)
secret = "63cusj7i63p2godikdf4qcpas65aqvvq"

# Generate 6-digit TOTP code
totp = pyotp.TOTP(secret)
print("Current TOTP code:", totp.now())


