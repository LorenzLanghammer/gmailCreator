from enterName import generateName, generateTextInsertion
from helper import addLines
import subprocess
import os
import pyautogui
import time
import webbrowser

#firstName, lastName = generateName()
firstNameIdentifier = "firstNameStart"
lastNameIdentifier = "lastNameStart"
enterNameFile = "enterNameTemplate.txt"

source_dir= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
chrome_path = r"C:\Programme\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))



webbrowser.get('chrome').open("https://www.google.com")
time.sleep(3)

pyautogui.write("google create account", interval=0.1)
pyautogui.press("enter")
time.sleep(3)

location = pyautogui.locateCenterOnScreen(os.path.join(source_dir, 'elementImages\createAccountResult.png'), confidence=0.8)

if location:
    pyautogui.moveTo(location.x, location.y, duration=0.5)
    pyautogui.click()
else:
    print("Target not found on screen")


def get_lines():
    with open ('enterNameTemplate.txt') as f:
        lines = f.readlines()
    return lines


#lines = get_lines()

# add first name to enterName.py

#firstNameLines = generateTextInsertion(firstName)
#addLines(lines, firstNameIdentifier, firstNameLines)

#add last name to eneterName.py
#lastNameLines = generateTextInsertion(lastName)







startChrome_script = os.path.join(source_dir, "ahkFiles\startChrome.ahk")


#subprocess.run([startChrome_script])







