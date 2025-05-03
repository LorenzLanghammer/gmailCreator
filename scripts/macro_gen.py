import pyautogui
import os
import webbrowser
import random
import math
import numpy as np
sqrt3 = np.sqrt(3)
sqrt5 = np.sqrt(5)

source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
chrome_path = r"C:\Programme\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

timeOffsetLowerBound = 0.000648996353149414
timeOffsetUpperBound = 0.02896112442016602

maxX = 1901
maxY = 998


def moveToPoint(start_x, start_y, dest_x, dest_y):
    G_0=9
    W_0=3
    M_0=15
    D_0=12
    
    events = []
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
        start_x += v_x
        start_y += v_y
        move_x = int(np.round(start_x))
        move_y = int(np.round(start_y))
        if current_x != move_x or current_y != move_y:
            #move_mouse(current_x:=move_x,current_y:=move_y)
            points.append([move_x, move_y])

    for i, point in enumerate(points):
        event = ""
        if (i == len(points) - 1):
            event = f'{{"type": "cursorMove","x": {point[0]},"y": {point[1]},"timestamp": {generateTimeOffset()}}}'
        else:
            event = f'{{"type": "cursorMove","x": {point[0]},"y": {point[1]},"timestamp": {generateTimeOffset()}}},'
        events.append(event)
    return events


def generateTimeOffset():
    return random.uniform(timeOffsetLowerBound, timeOffsetUpperBound)




def joinEvents(eventsList):
    result = []
    for i, events in enumerate(eventsList):
        for j, event in enumerate(events):
            if (i != len(eventsList) - 1 and j == len(eventsList[i]) - 1):
                result.append(event + ",")
            else:
                result.append(event)
    return result



    

def randomMouseMovement(currentX, currentY, targetX, targetY):
    num_points = random.randint(2, 4) + 1
    events = []

    startX = currentX
    startY = currentY
    newX = 0
    newY = 0

    for i in range(num_points):
        newX = random.randint(0, maxX)
        newY = random.randint(0, maxY)
        randomMovement = moveToPoint(startX, startY, newX, newY)
        startX = newX
        startY = newY
        events.append(randomMovement)
    lastMovement = moveToPoint(newX, newY, targetX, targetY)
    events.append(lastMovement)
    return joinEvents(events)


def type(text):
    events = []
    for i, char in enumerate(text):
        if (i == len(text) - 1):
            event = f'{{"type":"keyboardEvent","key":"{char}","timestamp":{generateTimeOffset()},"pressed":true}}, \n'
            events.append(event)
            event = f'{{"type":"keyboardEvent","key":"{char}","timestamp":{generateTimeOffset()},"pressed":false}} \n'
            events.append(event)
        else:
            event = f'{{"type":"keyboardEvent","key":"{char}","timestamp":{generateTimeOffset()},"pressed":true}}, \n'
            events.append(event)
            event = f'{{"type":"keyboardEvent","key":"{char}","timestamp":{generateTimeOffset()},"pressed":false}}, \n'
            events.append(event)

    return events

def click(x, y):
    events = []
    events.append(f'{{"type":"leftClickEvent","x":{x},"y":{y},"timestamp":0.09622859954833984,"pressed":true}},')
    events.append(f'{{"type":"leftClickEvent","x":{x},"y":{y},"timestamp":0.09622859954833984,"pressed":false}}')
    return events


def scrollDown(num_scrolls):
    events = []
    for i in range(num_scrolls):
        if (i == num_scrolls - 1):
            events.append(f'{{"type":"scrollEvent","dx":0,"dy":-1,"timestamp":{generateTimeOffset()}}}')
        else: 
            events.append(f'{{"type":"scrollEvent","dx":0,"dy":-1,"timestamp":{generateTimeOffset()}}},')
    return events

def pauseAt(x, y):
    events = []
    events.append(f'{{"type": "cursorMove","x": {x},"y": {y},"timestamp": {0.9}}}')
    return events