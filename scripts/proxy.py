from abc import ABC, abstractmethod
import json
import requests
import random
import string
import zendriver as zd
import asyncio
from country_values import *
from smsactivate.api import SMSActivateAPI
from helper import *
    

class Proxy(ABC):

    def __init__(self, country, region=None, city=None):
        self.country = country
        if region is not None:
            self.region = region
        if city is not None:
            self.city = city

    @abstractmethod
    def getProxy(self):
        pass

    @abstractmethod
    def getUsername(self):
        pass

    @abstractmethod
    def getPassword(self):
        pass

    @abstractmethod
    def getIp(self):
        pass

class RayobyteProxy(Proxy):

    def getProxy(self):
        return "la.residential.rayobyte.com:8000"
    
    def getUsername(self):
        return "lorenzlanghammer7_gmail_com"
    
    def getPassword(self):
        proxy_string = f"4R7rhACgPhG6udy-session-{generate_session_string()}-country-{CountryProxy[self.country].value.upper()}"
        #if self.region:
            #proxy_string +=  f"-region-{self.region}"
        #if self.city:
        #    proxy_string += f"-city-{self.city}"
        return proxy_string

    def getIp(self):
        return ""

class DecodoProxy(Proxy):
    def getProxy(self):
        proxy_host = "isp.decodo.com"
        proxy_port = 10001
        proxy = f"http://{proxy_host}:{proxy_port}"
        return proxy
    
    def getUsername(self):
        return f"user-spxcthqaa2-country-{CountryProxy[self.country].value}-{generate_session_string()}"
    
    def getPassword(self):
        return "Mz57jK9Wm=Mb4pattv"
    
    def getIp(self): 
        #resp = requests.get("https://api.ipify.org?format=json", proxies=proxies, timeout=10)
        return ""


class InfaticaProxy(Proxy):
    def getProxy(self):
            proxy_host = "pool.infatica.io"
            proxy_port = 10001
            proxy = f"http://{proxy_host}:{proxy_port}"
            return proxy

    def getUsername(self):
        return "7GPU0twSzoBJ6wbhsJjR"  

    def getPassword(self):
        return "Rx696vgQ"      

    def getIp(self):
        return ""  

