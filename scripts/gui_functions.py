import pyautogui
import os
import webbrowser
import random
import math
import time
import numpy as np
import zendriver as zd
import asyncio

sqrt3 = np.sqrt(3)
sqrt5 = np.sqrt(5)

source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
chrome_path = r"C:\Programme\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

timeOffsetLowerBound = 0.000648996353149414
timeOffsetUpperBound = 0.02896112442016602

maxX = 1901
maxY = 998

class ScreenPosition:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

def moveToPoint(dest_x, dest_y, speed):
    start_x = pyautogui.position().x
    start_y = pyautogui.position().y

    G_0=9
    W_0=3
    M_0=15
    D_0=12

    points = []

    current_x,current_y = start_x,start_y
    v_x = v_y = W_x = W_y = 0
    while (dist:=np.hypot(dest_x-start_x,dest_y-start_y)) >= 1:
        W_mag = min(W_0, dist)
        if dist >= D_0:
            W_x = W_x/sqrt3 + (2*np.random.random()-1)*W_mag/sqrt5
            W_y = W_y/sqrt3 + (2*np.random.random()-1)*W_mag/sqrt5
        else:
            W_x /= sqrt3
            W_y /= sqrt3
            if M_0 < 3:
                M_0 = np.random.random()*3 + 3
            else:
                M_0 /= sqrt5
        v_x += W_x + G_0*(dest_x-start_x)/dist
        v_y += W_y + G_0*(dest_y-start_y)/dist
        v_mag = np.hypot(v_x, v_y)
        if v_mag > M_0:
            v_clip = M_0/2 + np.random.random()*M_0/2
            v_x = (v_x/v_mag) * v_clip
            v_y = (v_y/v_mag) * v_clip
        dynamic_speed = speed * min(1.0, dist / D_0)  # D_0 is your decay threshold
        start_x += dynamic_speed*v_x
        start_y += dynamic_speed*v_y
        move_x = int(np.round(start_x))
        move_y = int(np.round(start_y))
        if current_x != move_x or current_y != move_y:
            #move_mouse(current_x:=move_x,current_y:=move_y)
            points.append([move_x, move_y])

    for i, point in enumerate(points):
        pyautogui.moveTo(point[0], point[1], duration=random.uniform(1/(1000*speed), 1/(100*speed)))


def generateTimeOffset():
    return random.uniform(timeOffsetLowerBound, timeOffsetUpperBound)



def randomMouseMovement(currentX, currentY, targetX, targetY):
    num_points = random.randint(2, 5)

    startX = currentX
    startY = currentY
    newX = 0
    newY = 0
    for i in range(num_points):
        if (i == num_points - 1):
            moveToPoint(startX, startY, targetX, targetY, 4)
        else:
            newX = random.randint(0, maxX)
            newY = random.randint(0, maxY)
            moveToPoint(startX, startY, newX, newY, 4)
            startX = newX
            startY = newY

async def get_position_by_selector(text, tab):
    await tab.wait_for_ready_state("complete", timeout=10)
    try:
        element = await tab.select(text)
    except:
        print("could not find element")
        return
    
    position = await element.get_position(abs=False)
    if position.width > 25:
        return ScreenPosition((position.x + 30) + position.width / 2, (position.y + 80) + position.height / 2)
    else:
        return ScreenPosition((position.x + 15), position.y + 90)


async def get_position_by_text(text, tab):
    await tab.wait_for_ready_state("complete", timeout=10)
    try:
        element = await tab.find_element_by_text(text, best_match=True)
        if not element:
            return
    except:
        print("could not find element")
        return
    position = await element.get_position(abs=False)
    return ScreenPosition((position.x + 35) + position.width / 2, (position.y + 85) + position.height / 2)
   


async def is_element_on_page(selector, tab):
    await tab.wait_for_ready_state("complete", timeout=10)

    try:
        element = await tab.select(selector)
    except:
        print("element is not on page")
        return False
    return True



def click(x, y):
    events = []
    return events


def scrollDown(num_scrolls):
    for _ in range(num_scrolls):
        pyautogui.scroll(-100)
        time.sleep(random.uniform(0.09, 0.4))


def pauseAt():
    pyautogui.sleep(random.uniform(0.1, 3))

def type(text):
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(0.05, 0.25))

scrollDown(4)

