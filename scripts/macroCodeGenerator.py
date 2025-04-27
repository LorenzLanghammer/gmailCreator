import pyautogui
import os
import webbrowser

source_dir= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
chrome_path = r"C:\Programme\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def findAndClick(element, currentX, currentY):
    location = pyautogui.locateCenterOnScreen(os.path.join(source_dir, f'elementImages\{element}'), confidence=0.8)






