import time
import pyautogui
from gui_functions import *
import pyscreeze
from helper import*


month_days = {
    "January": 31,
    "February": 28,  # Adjust for leap year if needed
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

name = generateName()


class Routine:
    def __init__(self):
        pass
    def executeRoutine():
        pass


class SearchPage_routine(Routine):
    def executeRoutine(self):
        with open (os.path.join(source_dir, "persistentValues\searchPage.json")) as f:
            data = json.load(f)
        try:
            location = pyscreeze.locateCenterOnScreen(os.path.join(source_dir, 'elementImages\cookiesAblehnen.png'), confidence=0.4)
            pyautogui.click(location)
            time.sleep(5)
        except:
            print("cookies not required")
        barLocation = pyautogui.locateCenterOnScreen(os.path.join(source_dir, 'elementImages\searchBar.png'), confidence=0.6)
        time.sleep(1)
        pyautogui.moveTo(barLocation)
        pyautogui.click(barLocation)
        time.sleep(1)
        pyautogui.write("create gmail account", interval=0.1)
        pyautogui.press("enter")
        time.sleep(1)
        moveToPoint(0, 0, data["google_resultX"], data["google_resultY"], 2)
        pauseAt()
        pyautogui.click()
        pauseAt()

class GotoPage_routine(Routine):
    def executeRoutine(self):
        with open (os.path.join(source_dir, "persistentValues\searchPage.json")) as f:
            data = json.load(f)
        randomMouseMovement(pyautogui.position().x, pyautogui.position().y, random.uniform(100, 400), random.uniform(100, 500))
        scrollDown(random.randint(5, 8))
        buttonLocation = pyautogui.locateCenterOnScreen(os.path.join(source_dir, 'elementImages\createAccountbutton.png'), confidence=0.7)
        time.sleep(1)
        moveToPoint(pyautogui.position().x, pyautogui.position().y, buttonLocation[0], buttonLocation[1], 2)
        pyautogui.click()

class SelectAccountType_routine(Routine):
    def executeRoutine(self):
        with open (os.path.join(source_dir, "persistentValues\selectAccountType.json")) as f:
            data = json.load(f)
        moveToPoint(pyautogui.position().x, pyautogui.position().y, data["erstellenX"], data["erstellenY"], 3)
        time.sleep(1)
        pyautogui.click()
        moveToPoint(pyautogui.position().x, pyautogui.position().y, data["privateNutzungX"], data["privateNutzungY"], 2)
        moveToPoint(pyautogui.position().x, pyautogui.position().y, data["kindX"], data["kindY"], 2)
        moveToPoint(pyautogui.position().x, pyautogui.position().y, data["arbeitX"], data["arbeitY"], 2)
        moveToPoint(pyautogui.position().x, pyautogui.position().y, data["kindX"], data["kindY"], 2)
        moveToPoint(pyautogui.position().x, pyautogui.position().y, data["privateNutzungX"], data["privateNutzungY"], 2)
        pyautogui.click()
        time.sleep(3)

class EnterName_routine(Routine):
    def executeRoutine(self):
        with open (os.path.join(source_dir, "persistentValues\enterName.json")) as f:
            data = json.load(f)
        firstName = name[0]
        lastName = name[1]

        moveToPoint(pyautogui.position().x, pyautogui.position().y, data["firstNameX"], data["firstNameY"], 2)
        pyautogui.click()
        type(firstName)
        moveToPoint(pyautogui.position().x, pyautogui.position().y, data["lastNameX"], data["lastNameY"], 2)
        pyautogui.click()
        type(lastName)
        moveToPoint(pyautogui.position().x, pyautogui.position().y, data["weiterButtonX"], data["weiterButtonY"], 2)
        pyautogui.click()
        time.sleep(3)


class EnterDateAndGender_routine(Routine):
    def executeRoutine(self):
        gender = name[2]
        month = random.choice(list(month_days.keys()))
        month_position = month_positions[month]
        day = random.randint(1, month_days[month])
        year = random.randint(1970, 2004)
        with open (os.path.join(source_dir, "persistentValues\enterDateAndGender.json")) as f:
            data = json.load(f)
        moveToPoint(pyautogui.position().x, pyautogui.position().y, data["tagX"], data["tagY"], 2)
        pyautogui.click()
        pauseAt()
        type(f'{day}')
        pauseAt()
        moveToPoint(pyautogui.position().x, pyautogui.position().y, data["monatX"], data["monatY"], 2)
        pyautogui.click()
        pauseAt()
        moveToPoint(pyautogui.position().x, pyautogui.position().y, data["monatX"], month_position, 2)
        pyautogui.click()
        pauseAt()
        moveToPoint(pyautogui.position().x, pyautogui.position().y, data["jahrX"], data["jahrY"], 2)
        pyautogui.click()
        pauseAt()
        type(f'{year}')
        moveToPoint(pyautogui.position().x, pyautogui.position().y, data["genderX"], data["genderY"], 2)
        pyautogui.click()
        if (gender == "male"):
            moveToPoint(pyautogui.position().x, pyautogui.position().y, data["maleX"], data["maleY"], 2)
        else:
            moveToPoint(pyautogui.position().x, pyautogui.position().y, data["maleX"], data["maleY"], 2)
        pyautogui.click()
        moveToPoint(pyautogui.position().x, pyautogui.position().y, data["weiterButtonX"], data["weiterButtonY"], 2)
        pyautogui.click()
        time.sleep(3)


class SelectAddressType_routine(Routine):
    def executeRoutine(self):
        with open (os.path.join(source_dir, "persistentValues\selectAddressType.json")) as f:
            data = json.load(f)
        pauseAt()
        moveToPoint(pyautogui.position().x, pyautogui.position().y, data["adresseErstellenX"], data["adresseErstellenY"], 2)
        pyautogui.click()
        moveToPoint(pyautogui.position().x, pyautogui.position().y, data["weiterButtonX"], data["weiterButtonY"], 2)
        pyautogui.click()

class SelectAddress_routine(Routine):
    def executeRoutine(self):
        with open (os.path.join(source_dir, "persistentValues\selectAddress.json")) as f:
            data = json.load(f)
        if(random.randint(0, 1) == 0):
            moveToPoint(pyautogui.position().x, pyautogui.position().y, data["firstAddressX"], data["firstAddressY"], 2)
            pyautogui.click()
        else: 
            moveToPoint(pyautogui.position().x, pyautogui.position().y, data["secondAddressX"], data["secondAddressY"], 2)
            pyautogui.click()
            pauseAt()
        moveToPoint(pyautogui.position().x, pyautogui.position().y, data["weiterButtonX"], data["weiterButtonY"], 2)
        pauseAt()






