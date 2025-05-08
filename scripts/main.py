import time
import webbrowser
from gui_functions import *
from helper import *
import json
import os
import pyautogui
import subprocess
import pyscreeze
from routine import *
from selenium import webdriver


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
chrome_path = r"C:\Programme\Google\Chrome\Application\chrome.exe"
firefox_path = r"C:\Programme\Mozilla Firefox\firefox.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))


name = generateName()
firstName = name[0]
lastName = name[1]
gender = name[2]
month = random.choice(list(month_days.keys()))
month_position = month_positions[month]
day = random.randint(1, month_days[month])
year = random.randint(1970, 2004)

source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
maxX = 1901
maxY = 998

with open (os.path.join(source_dir, "persistentValues\searchPage.json")) as f:
    data = json.load(f)

webbrowser.get('firefox').open("https://www.google.com")
time.sleep(3)


routines = [SearchPage_routine(), 
            GotoPage_routine(), 
            SelectAccountType_routine(),
            EnterName_routine(), 
            EnterDateAndGender_routine(), 
            SelectAddressType_routine(), 
            SelectAddress_routine()
            ]

#for routine in routines: 
#   routine.executeRoutine()