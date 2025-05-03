from gui_functions import *
from helper import *
import json
import os
import pyautogui
import time
import subprocess
import pyscreeze


source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
chrome_path = r"C:\Programme\Google\Chrome\Application\chrome.exe"
firefox_path = r"C:\Programme\Mozilla Firefox\firefox.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))



source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
maxX = 1901
maxY = 998


class Routine:
    def __init__(self, currentX, currentY):
        self.currentX = currentX
        self.currentY = currentY
    def generateMacroCodes(self):
        pass
    def execute_routine(self):
        pass

class OpenPageRoutine(Routine):
   
    def execute_routine(self):
        with open (os.path.join(source_dir, "persistentValues\openPage.json")) as f:
            data = json.load(f)
        webbrowser.get('firefox').open("https://www.google.com")
        time.sleep(3)
        try:
            location = pyscreeze.locateCenterOnScreen(os.path.join(source_dir, 'elementImages\cookiesAblehnen.png'), confidence=0.4)
            pyautogui.click(location)
            time.sleep(5)
        except:
            print("cookies not required")
        barLocation = pyautogui.locateCenterOnScreen(os.path.join(source_dir, 'elementImages\searchBar.png'), confidence=0.4)
        time.sleep(1)
        pyautogui.moveTo(barLocation)
        pyautogui.click(barLocation)
        time.sleep(1)
        pyautogui.write("create gmail account", interval=0.1)
        pyautogui.press("enter")
        time.sleep(1)
        moveToPoint(0, 0, data["google_resultX"], data["google_resultY"])
        pauseAt()
        pyautogui.click()
        pauseAt()


openPageRout = OpenPageRoutine(0, 0)

openPageRout.execute_routine()



















