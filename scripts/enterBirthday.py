import os
import webbrowser
import time
import pyautogui

source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
chrome_path = r"C:\Programme\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

webbrowser.get('chrome').open("https://www.google.com")
time.sleep(10)

img_path = os.path.join(source_dir, "elementImages", "test.png")
location = pyautogui.locateCenterOnScreen(img_path, confidence=0.6)
print(location)

