import time
import pyautogui as pag
from gui_functions import *
import pyscreeze
from helper import*
import zendriver as zd
import asyncio



month_days = {
    1: 31,
    2: 28, 
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

month_offsets = {
    "January": 515,
    "February": 545,
    "March": 575,
    "April": 600,
    "May": 630,
    "June": 660,
    "July": 689,
    "August": 715,
    "September": 744,
    "October": 772
}

name = generateName()


class Routine:
    def __init__(self, tab):
        self.tab = tab
    async def executeRoutine(self):
        pass


class SearchPage_routine(Routine):
    async def executeRoutine(self):
        accept_position = await get_position_by_selector("#L2AGLb", self.tab)
        moveToPoint(pag.position().x, pag.position().y , accept_position.x, accept_position.y, 2)
        pag.click()

        searchBar_position = await get_position_by_selector('[aria-label="Suche"]', self.tab)
        moveToPoint(pag.position().x, pag.position().y, searchBar_position.x, searchBar_position.y, 2)
        pauseAt()
        pag.click()

        type("create gmail account")
        pag.press("enter")

        await self.tab.wait_for_ready_state("complete", timeout=10)
        googleResult_position = await get_position_by_selector("h3.LC20lb", self.tab)
        pauseAt()
        moveToPoint(pag.position().x, pag.position().y, googleResult_position.x, googleResult_position.y, 2)
        pag.click()



class GotoPage_routine(Routine):
    async def executeRoutine(self):
        randomMouseMovement(pag.position().x, pag.position().y, random.uniform(100, 400), random.uniform(100, 500))
        scrollDown(random.randint(5, 8))

        buttonLocation = await get_position_by_text("Create an account", self.tab)
        moveToPoint(pag.position().x, pag.position().y, buttonLocation.x, buttonLocation.y, 2)
        pag.click()



class SelectAccountType_routine(Routine):
    async def executeRoutine(self):
    
        await asyncio.sleep(1)
        erstellen_position = await get_position_by_text('Konto erstellen', self.tab)        
        moveToPoint(pag.position().x, pag.position().y, erstellen_position.x, erstellen_position.y, 3)
        pag.click()

        private_nutzung_position = await get_position_by_selector('[jsname="K4r5Ff"]', self.tab)
        moveToPoint(pag.position().x, pag.position().y, private_nutzung_position.x, private_nutzung_position.y, 3)

        kind_position = await get_position_by_selector('[jsname="IfUHnf"]', self.tab)
        moveToPoint(pag.position().x, pag.position().y, kind_position.x, kind_position.y, 3)

        arbeit_position = await get_position_by_selector('[jsname="iAUJgf"]', self.tab)
        moveToPoint(pag.position().x, pag.position().y, arbeit_position.x, arbeit_position.y, 3)
        moveToPoint(pag.position().x, pag.position().y, kind_position.x, kind_position.y, 3)
        moveToPoint(pag.position().x, pag.position().y, private_nutzung_position.x, private_nutzung_position.y, 3)
        pag.click()


class EnterName_routine(Routine):
    async def executeRoutine(self):

        firstName = name[0]
        lastName = name[1]

        first_name_position = await get_position_by_selector("#firstName", self.tab)
        moveToPoint(pag.position().x, pag.position().y,first_name_position.x, first_name_position.y, 2)
        pag.click()
        type("test")

        last_name_position = await get_position_by_selector("#lastName", self.tab)
        moveToPoint(pag.position().x, pag.position().y, last_name_position.x, last_name_position.y, 2)
        pag.click()
        type("test")

        weiter_button_position = await get_position_by_selector('[jsname="V67aGc"]', self.tab)
        moveToPoint(pag.position().x, pag.position().y, weiter_button_position.x, weiter_button_position.y, 2)
        pag.click()


class EnterDateAndGender_routine(Routine):
    async def executeRoutine(self):

        gender = name[2]
        month = random.randint(1, 12)
        day = random.randint(1, month_days[month])
        year = random.randint(1970, 2004)


        day_position = await get_position_by_selector("#day", self.tab)
        moveToPoint(pag.position().x, pag.position().y, day_position.x, day_position.y, 2)
        pag.click()
        pauseAt()
        type(f'{day}')
        pauseAt()

        month_position = await get_position_by_selector(".VfPpkd-aPP78e", self.tab)
        moveToPoint(pag.position().x, pag.position().y, month_position.x, month_position.y, 2)
        pag.click()
        january_position = await get_position_by_selector('.VfPpkd-xl07Ob-XxIAqe-OWXEXe-FNFY6c > ul:nth-child(1) > li:nth-child(2)', self.tab)
        moveToPoint(pag.position().x, pag.position().y, january_position.x, january_position.y, 2)

        if month >= 11:
            scrollDown(3)
        
        selected_month_position = await get_position_by_selector(f'.VfPpkd-xl07Ob-XxIAqe-OWXEXe-FNFY6c > ul:nth-child(1) > li:nth-child({month + 1})', self.tab)
        moveToPoint(pag.position().x, pag.position().y, selected_month_position.x, selected_month_position.y, 2)
        pag.click()

        year_position = await get_position_by_selector('#year', self.tab)
        moveToPoint(pag.position().x, pag.position().y, year_position.x, year_position.y, 2)
        pag.click()
        pauseAt()
        type(f'{year}')
        
        gender_position = await get_position_by_selector('#gender', self.tab)
        moveToPoint(pag.position().x, pag.position().y, gender_position.x, gender_position.y, 2)
        pag.click()

        female_position = await get_position_by_selector('.VfPpkd-xl07Ob-XxIAqe-OWXEXe-FNFY6c > ul:nth-child(1) > li:nth-child(2)', self.tab)
        male_position = await get_position_by_selector('.VfPpkd-xl07Ob-XxIAqe-OWXEXe-FNFY6c > ul:nth-child(1) > li:nth-child(3)', self.tab)

        if (gender == "male"):
            moveToPoint(pag.position().x, pag.position().y, male_position.x, male_position.y, 2)
        else:
            moveToPoint(pag.position().x, pag.position().y, female_position.x, female_position.y, 2)
        
        pag.click()

        weiter_position = await get_position_by_selector('#birthdaygenderNext', self.tab)
        moveToPoint(pag.position().x, pag.position().y, weiter_position.x, weiter_position.y, 2)
        pag.click()



class SelectAddressType_routine(Routine):
    async def executeRoutine(self):
        adresse_erstellen_position = await get_position_by_selector('[jsname="ornU0b"]', self.tab)
        moveToPoint(pag.position().x, pag.position().y, adresse_erstellen_position.x, adresse_erstellen_position.y, 2)
        pag.click()

        weiter_position = await get_position_by_selector('.VfPpkd-dgl2Hf-ppHlrf-sM5MNb', self.tab)
        moveToPoint(pag.position().x, pag.position().y, weiter_position.x, weiter_position.y, 2)
        pag.click()
        pauseAt()



class SelectAddress_routine(Routine):
    async def executeRoutine(self):

        name_field_position = await get_position_by_text('Nutzername', self.tab)
        if name_field_position:
            print("found address field")
            moveToPoint(pag.position().x, pag.position().y, name_field_position.x + 20, name_field_position.y + 20, 2)
            pag.click()
            pauseAt()
            type(generateEmail(name[0], name[1], 0))
            pag.press("enter")

        else:
            print("did not find address field")
            moveToPoint(pag.position().x, pag.position().y, 993, 451, 2)
            pag.click()



class EnterPassword_routine(Routine):
    async def executeRoutine(self):
        password = generate_password(random.randint(8, 15))
        
        password_position = await get_position_by_selector("#passwd", self.tab)
        moveToPoint(pag.position().x, pag.position().y, password_position.x, password_position.y, 2)
        pag.click()
        type(password)

        confirm_position = await get_position_by_selector("#confirm-passwd", self.tab)
        moveToPoint(pag.position().x, pag.position().y, confirm_position.x, confirm_position.y, 2)
        pag.click()
        type(password)
        pauseAt()

        weiter_position = await get_position_by_selector("#createpasswordNext", self.tab)
        moveToPoint(pag.position().x, pag.position().y, weiter_position.x, weiter_position.y, 2)
        pag.click()
        pauseAt()


'''
with open (os.path.join(source_dir, "persistentValues\selectAddress.json")) as f:
    data = json.load(f)
if(random.randint(0, 1) == 0):
    moveToPoint(pag.position().x, pag.position().y, data["firstAddressX"], data["firstAddressY"], 2)
    pag.click()
else: 
    moveToPoint(pag.position().x, pag.position().y, data["secondAddressX"], data["secondAddressY"], 2)
    pag.click()
    pauseAt()
moveToPoint(pag.position().x, pag.position().y, data["weiterButtonX"], data["weiterButtonY"], 2)
pauseAt()

'''

