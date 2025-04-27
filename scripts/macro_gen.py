import pyautogui
import os
import webbrowser
import random
import math

source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
chrome_path = r"C:\Programme\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))


def findAndClick(element, currentX, currentY):
    location = pyautogui.locateCenterOnScreen(os.path.join(source_dir, f'elementImages\{element}'), confidence=0.8)
    events = []

    distance = math.hypot(location.x - currentX, location.y - currentY)
    base_points = int(distance / 50)
    num_points = random.randint(base_points, base_points + 10)
    points = []

    for i in range (num_points + 1):
        t = i / num_points
        x = currentX + (location.x - currentX) * t
        y = currentY + (location.y - currentY) * t

        offset_x = random.uniform(-5, 5) * math.sin(math.pi * t)
        offset_y = random.uniform(-5, 5) * math.sin(math.pi * t)

        points.append((x + offset_x, y + offset_y))

    for point in points:
        event = f'{{"type": "cursorMove","x": {point[0]},"y": {point[1]},"timestamp": 0.008074522018432617}}'
        events.append(event)

    print(events)

findAndClick('testpy.png', 25, 25)



