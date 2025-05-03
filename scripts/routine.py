from macro_gen import *
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
    def generateMacroCodes(self):
        with open(os.path.join(source_dir, "persistentValues\openPage.json"), "r") as f:
            data = json.load(f)
        moveToGoogleResult = moveToPoint(0, 0, data["google_resultX"], data["google_resultY"])
        clickGoogleResult = click(data["google_resultX"], data["google_resultY"])
        moveRandomly = randomMouseMovement(data["google_resultX"], data["google_resultY"], data["google_resultX"], data["google_resultY"])
        clickWindow = click(data["google_resultX"], data["google_resultY"])
        scroll = scrollDown(data["num_scrolls"])
        moveToCreate = moveToPoint(data["google_resultX"], data["google_resultY"], data["createX"], data["createY"])
        clickCreate = click(data["createX"], data["createY"])
        randomX = random.randint(data["createX"], data["createX"] + 200)
        randomY = random.randint(data["createY"], data["createY"] + 200)
        moveRandomly= randomMouseMovement(data["createX"], data["createY"], randomX, randomY)
        moveToErstellen = moveToPoint(randomX, randomY, data["erstellenX"], data["erstellenY"])
        clickErstellen = click(data["erstellenX"], data["erstellenY"])
        moveToPrivateNutzung = moveToPoint(data["erstellenX"], data["erstellenY"], data["privateNutzungX"], data["privateNutzungY"])
        moveToKind = moveToPoint(data["erstellenX"], data["erstellenY"], data["kindX"], data["kindY"])
        moveToArbeit = moveToPoint(data["kindX"], data["kindY"], data["arbeitX"], data["arbeitY"])
        pause = pauseAt(data["arbeitX"], data["arbeitY"])
        moveBackToPrivateNutzung = moveToPoint(data["arbeitX"], data["arbeitY"], data["privateNutzungX"], data["privateNutzungY"])
        clickPrivateNutzung = click(data["privateNutzungX"], data["privateNutzungY"])
        result = joinEvents([moveToGoogleResult, 
                             clickGoogleResult, 
                             moveRandomly, 
                             clickWindow, 
                             scroll, moveToCreate, clickCreate, 
                             moveToErstellen, clickErstellen, moveToPrivateNutzung, moveToKind, moveToArbeit, pause, moveBackToPrivateNutzung, clickPrivateNutzung])

        with open (os.path.join(source_dir, "macroScripts\openPage.pmr"), "w") as f:
            f.write('{"events": [ \n')
            for event in result:
                f.write(event + "\n")
            f.write(']}')
        return ([data["privateNutzungX"], data["privateNutzungY"]])
    def execute_routine(self):
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
        openPage_script = os.path.join(source_dir, "ahkFiles\openPage.exe")
        subprocess.run([openPage_script])
    

class EnterNameRoutine(Routine):
    def generateMacroCodes(self):
        name = generateName()
        with open(os.path.join(source_dir, "persistentValues\enterName.json"), "r") as f:
            data = json.load(f)
        randomTargetX = random.randint(0, maxX)
        randomTargetY = random.randint(0, maxY)
        moveToFirstName = moveToPoint(self.currentX, self.currentY, data["firstNameX"], data["firstNameY"])
        clickFirstName = click(data["firstNameX"], data["firstNameY"])
        typeFirstName = type(name[0])
        moveRandomly = randomMouseMovement(data["firstNameX"], data["firstNameY"], randomTargetX, randomTargetY)
        moveToLastName = moveToPoint(randomTargetX, randomTargetY, data["lastNameX"], data["lastNameY"])
        clickLastName = click(data["lastNameX"], data["lastNameY"])
        typeLastName = type(name[1])

        result = joinEvents([moveToFirstName, clickFirstName, typeFirstName, moveRandomly, moveToLastName, clickLastName, typeLastName])

        with open (os.path.join(source_dir, "macroScripts\enterName.pmr"), "w") as f:
            f.write('{"events": [ \n')
            for event in result:
                f.write(event + "\n")
            f.write(']}')
        return ([data["lastNameX"], data["lastNameY"]])

openPageRout = OpenPageRoutine(0, 0)
openPagePos = openPageRout.generateMacroCodes()

enterNameRout = EnterNameRoutine(openPagePos[0], openPagePos[1])
enterNamePos = enterNameRout.generateMacroCodes()

openPageRout.execute_routine()
#enterNameRout.execute_routine()

































