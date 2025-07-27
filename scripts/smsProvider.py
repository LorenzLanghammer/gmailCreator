from abc import ABC, abstractmethod
import json
import requests
import random
import string
import zendriver as zd
import asyncio
from country_values import *
from smsactivate.api import SMSActivateAPI




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


class SmsProvider(ABC):
    @abstractmethod
    async def getPhoneNumber(self):
        pass

    @abstractmethod
    async def checkStatus(self, number_id):
        pass

    @abstractmethod
    async def cancelOrder(self, number_id):
        pass


class SmsActivate(SmsProvider):
    api_key = "8318bf02e3cf43fA9727fe18d21063bc"

    async def getPhoneNumber(self, country):
        request_params = {  'api_key': api_key, 
                        'action': 'getNumber',
                        'service': 'go', 
                        'country': 13, 
                        'operator': 'any'
                        }
        response = requests.get(f"https://sms-activate.org/stubs/handler_api.php", params=request_params)
        if response.status_code == 200:
            parts = response.text.split(':')
            if parts[0] == 'ACCESS_NUMBER':
                activation_id = parts[1]
                phone_number = parts[2]
                return Number(id=activation_id, number="+972" + phone_number)
            else: 
                print("Error: ", response.text)
                return None
        else:
            print("Http error: ", response.status_code)
            return None
        
    
    async def checkStatus(self, number_id):
        def get_status():
            return sa.getStatus(id=number_id)
        
        status = await asyncio.to_thread(get_status)
        
        if status.startswith("STATUS_OK:"):
            return status.split(":")[1]
        
        elif status == "STATUS_WAIT_CODE":
            print("Status:", status)
            return None

    async def cancelOrder(self, number_id):
        return



class VSim(SmsProvider):
    api_key = "93NgGYtBW7EYX5y-418a38vT-k4PU8n6p-fA22NLZn-RnL1p38p2NTz937"
    
    async def getPhoneNumber(self, country):
        request_params = {  'api_key': api_key, 
                        'service': 'google', 
                        #'country': CountryNumber[country].value, 
                        'country': 30,
                        'number': 'true',
                        'lang': 'en'
                        }
        
        response = requests.get(f"https://onlinesim.io/api/getNum.php", params=request_params)
        print(response)
        
    
    async def checkStatus(self, number_id):
        def get_status():
            return sa.getStatus(id=number_id)
        
        status = await asyncio.to_thread(get_status)
        
        if status.startswith("STATUS_OK:"):
            return status.split(":")[1]
        
        elif status == "STATUS_WAIT_CODE":
            print("Status:", status)
            return None

    async def cancelOrder(self):
        return


    
    async def checkStatus(self, number_id):
        return await super().checkStatus(number_id)
    
    async def cancelOrder(self, number_id):
        return await super().cancelOrder()
    


class DaisySim(SmsProvider):
    api_key = "dJ2cDFrv8QVwDo0WEoWXrs2QaYHGuI"

    async def getPhoneNumber(self, country):

        request_params = {  'api_key': "dJ2cDFrv8QVwDo0WEoWXrs2QaYHGuI", 
                            'action': 'getNumber',
                            'service': 'go',
                            'carrier': 'att'
                            }
            
        response = requests.get(f"https://daisysms.com/stubs/handler_api.php", params=request_params)
        print(response.text)
        
        if response.status_code == 200:
            parts = response.text.split(':')
            if parts[0] == 'ACCESS_NUMBER':
                activation_id = parts[1]
                phone_number = parts[2]
                return Number(id=activation_id, number="+1"+phone_number)
            else:
                print("Error: ", response.text)
                return None
        else:
            print("Http error: ", response.status_code)
            return None
    
    
    async def checkStatus(self, number_id):
        request_params = {  'api_key': "dJ2cDFrv8QVwDo0WEoWXrs2QaYHGuI", 
                            'action': 'getStatus',
                            'id': number_id
                            }
        def get_status():
            response = requests.get(f"https://daisysms.com/stubs/handler_api.php", params=request_params)
            return response.text
        
        status = await asyncio.to_thread(get_status)
        print(status)
        
        if status.startswith("STATUS_OK:"):
            return status.split(":")[1]
        
        elif status == "STATUS_WAIT_CODE":
            print("Status:", status)
            return None



    async def cancelOrder(self, number_id):

        request_params = {  'api_key': "dJ2cDFrv8QVwDo0WEoWXrs2QaYHGuI", 
                            'action': 'setStatus',
                            'status': 8,
                            'id': number_id
                            }
        
        response = requests.get(f"https://daisysms.com/stubs/handler_api.php", params=request_params)
        print(response.text)
        return



async def test():
    api_key = "dJ2cDFrv8QVwDo0WEoWXrs2QaYHGuI"
    request_params = {  'api_key': api_key, 
                                'action': 'getStatus',
                                'id': 299571543
                                }
    def get_status():
        response = requests.get(f"https://daisysms.com/stubs/handler_api.php", params=request_params)
        return response
            
    status = await asyncio.to_thread(get_status)
    
    if status.startswith("STATUS_OK:"):
        return status.split(":")[1]
    
    elif status == "STATUS_WAIT_CODE":
        print("Status:", status)
        return None
        



