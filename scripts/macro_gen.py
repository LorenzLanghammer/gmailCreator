import pyautogui
import os
import webbrowser
import random
import math

source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
chrome_path = r"C:\Programme\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

timeOffsetLowerBound = 0.000648996353149414
timeOffsetUpperBound = 0.08896112442016602

maxX = 1901
maxY = 998



def generateTimeOffset():
    return random.uniform(timeOffsetLowerBound, timeOffsetUpperBound)


def findAndMove(currentX, currentY, targetX, targetY):
    events = []

    distance = math.hypot(targetX - currentX, targetY - currentY)
    base_points = int(distance / 20)
    num_points = random.randint(base_points, base_points + 10)
    points = []

    for i in range (num_points + 1):
        t = i / num_points
        x = currentX + (targetX - currentX) * t
        y = currentY + (targetY - currentY) * t

        offset_x = random.uniform(-7, 7) * math.sin(math.pi * t)
        offset_y = random.uniform(-7, 7) * math.sin(math.pi * t)

        points.append((int(x + offset_x), int(y + offset_y)))

    for i, point in enumerate(points):
        event = ""
        if (i == len(points) - 1):
            event = f'{{"type": "cursorMove","x": {point[0]},"y": {point[1]},"timestamp": {generateTimeOffset()}}}'
        else:
            event = f'{{"type": "cursorMove","x": {point[0]},"y": {point[1]},"timestamp": {generateTimeOffset()}}},'
        events.append(event)
    return events

def joinEventsComma(events1, events2):
    events = []
    for i, event in enumerate(events1): 
        events.append(event + ",")
    for i, event in enumerate(events2):
        if (i != len(events2) -1):
            events.append(event + ",")
        else:
            events.append(event)
    return events

def joinEvents(eventsList):
    result = []
    for i, events in enumerate(eventsList):
        for j, event in enumerate(events):
            if (i != len(eventsList) - 1 and j == len(eventsList[i]) - 1):
                result.append(event + ",")
            else:
                result.append(event)
    return result


def findAndMoveOvershoot(element, currentX, currentY):
    location = pyautogui.locateCenterOnScreen(os.path.join(source_dir, f'elementImages\{element}'), confidence=0.8)
    findAndMoveOvershootPoint(currentX, currentY, location.x, location.y)

def findAndMoveOvershootPoint(currentX, currentY, targetX, targetY):
    distance = math.dist([currentX, currentY], [targetX, targetY])
    offset = 1.1 + 100/distance
    overShootPoint = [currentX + (targetX - currentX) * (offset), currentY + (targetY - currentY) * (offset)]
    moveToOvershoot = findAndMove(currentX, currentY, overShootPoint[0], overShootPoint[1])
    moveToTarget = findAndMove(overShootPoint[0], overShootPoint[1], targetX, targetY)
    result = joinEvents([moveToOvershoot, moveToTarget])
    return joinEvents([moveToOvershoot, moveToTarget])
    

def randomMouseMovement(currentX, currentY, targetX, targetY):
    num_points = random.randint(3, 7) + 1
    events = []

    startX = currentX
    startY = currentY
    newX = 0
    newY = 0

    for i in range(num_points):
        newX = random.randint(0, maxX)
        newY = random.randint(0, maxY)
        randomMovement = findAndMove(startX, startY, newX, newY)
        startX = newX
        startY = newY
        events.append(randomMovement)
    lastMovement = findAndMove(newX, newY, targetX, targetY)
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
