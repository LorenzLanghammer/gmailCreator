import time
import pyautogui as pag
from gui_functions import *
import pyscreeze
from helper import*
import zendriver as zd
import asyncio
from fiveSim import *



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

class EnterCredentials_routine(Routine):
    def __init__(self, tab, proxy_username, proxy_password):
        super().__init__(tab)
        self.proxy_username = proxy_username
        self.proxy_password = proxy_password

    async def executeRoutine(self):
        moveToPoint(917, 222, 2)
        pyautogui.click()
        pyautogui.write(self.proxy_username)

        moveToPoint(969, 276, 2)
        pyautogui.click()
        pyautogui.write(self.proxy_password)
        pyautogui.press("enter")
    
        moveToPoint(954, 339, 2)
        pyautogui.click()

        moveToPoint(1726, 62, 2)
        pag.click()

class SearchPage_routine(Routine):
    async def executeRoutine(self):
        accept_position = await get_position_by_selector("#L2AGLb", self.tab)
        moveToPoint( accept_position.x, accept_position.y, 2)
        pag.click()

        searchBar_position = await get_position_by_selector('#APjFqb', self.tab)
        moveToPoint(searchBar_position.x, searchBar_position.y, 2)
        pauseAt()
        pag.click()

        type("create gmail account")
        pag.press("enter")

        googleResult_position = await get_position_by_selector("h3", self.tab)
        pauseAt()
        moveToPoint(googleResult_position.x, googleResult_position.y, 2)
        pag.click()



class GotoPage_routine(Routine):
    async def executeRoutine(self):
        randomMouseMovement(random.uniform(100, 400), random.uniform(100, 500))
        scrollDown(random.randint(5, 8))

        buttonLocation = await get_position_by_selector("#page-width-container > div.main-content > article > section > div > div.article-content-container > div > p:nth-child(5) > a", self.tab)
        moveToPoint(buttonLocation.x, buttonLocation.y, 2)
        pag.click()



class SelectAccountType_routine(Routine):
    async def executeRoutine(self):
    
        await asyncio.sleep(1)
        #erstellen_position = await get_position_by_text('Utwórz konto', self.tab)        
        erstellen_position = await get_position_by_selector('#yDmH0d > c-wiz > div > div.JYXaTc > div > div.FO2vFd > div > div > div:nth-child(1) > div > button > span', self.tab)
        moveToPoint(erstellen_position.x, erstellen_position.y, 3)
        pag.click()

        private_nutzung_position = await get_position_by_selector('[jsname="K4r5Ff"]', self.tab)
        moveToPoint(private_nutzung_position.x, private_nutzung_position.y, 3)

        kind_position = await get_position_by_selector('[jsname="IfUHnf"]', self.tab)
        moveToPoint(kind_position.x, kind_position.y, 3)

        arbeit_position = await get_position_by_selector('[jsname="iAUJgf"]', self.tab)
        moveToPoint(arbeit_position.x, arbeit_position.y, 3)
        moveToPoint(kind_position.x, kind_position.y, 3)
        moveToPoint(private_nutzung_position.x, private_nutzung_position.y, 3)
        pag.click()


class EnterName_routine(Routine):
    async def executeRoutine(self):

        firstName = name[0]
        lastName = name[1]

        first_name_position = await get_position_by_selector("#firstName", self.tab)
        moveToPoint(first_name_position.x, first_name_position.y, 2)
        pag.click()
        type(firstName)
        #type("test")

        last_name_position = await get_position_by_selector("#lastName", self.tab)
        moveToPoint(last_name_position.x, last_name_position.y, 2)
        pag.click()
        type(lastName)
        #type("test")

        weiter_button_position = await get_position_by_selector('[jsname="V67aGc"]', self.tab)
        moveToPoint(weiter_button_position.x, weiter_button_position.y, 2)
        pag.click()


class EnterDateAndGender_routine(Routine):
    async def executeRoutine(self):

        gender = name[2]
        month = random.randint(1, 12)
        day = random.randint(1, month_days[month])
        year = random.randint(1970, 2004)


        day_position = await get_position_by_selector("#day", self.tab)
        moveToPoint(day_position.x, day_position.y, 2)
        pag.click()
        pauseAt()
        type(f'{day}')
        pauseAt()

        month_position = await get_position_by_selector(".VfPpkd-aPP78e", self.tab)
        moveToPoint(month_position.x, month_position.y, 2)
        pag.click()
        january_position = await get_position_by_selector('.VfPpkd-xl07Ob-XxIAqe-OWXEXe-FNFY6c > ul:nth-child(1) > li:nth-child(2)', self.tab)
        moveToPoint(january_position.x, january_position.y, 2)

        if month >= 11:
            scrollDown(3)

        selected_month_position = await get_position_by_selector(f'.VfPpkd-xl07Ob-XxIAqe-OWXEXe-FNFY6c > ul:nth-child(1) > li:nth-child({month + 1})', self.tab)
        moveToPoint(selected_month_position.x, selected_month_position.y, 2)
        pag.click()

        year_position = await get_position_by_selector('#year', self.tab)
        moveToPoint(year_position.x, year_position.y, 2)
        pag.click()
        pauseAt()
        type(f'{year}')
        
        gender_position = await get_position_by_selector('#gender', self.tab)
        moveToPoint(gender_position.x, gender_position.y, 2)
        pag.click()

        female_position = await get_position_by_selector('.VfPpkd-xl07Ob-XxIAqe-OWXEXe-FNFY6c > ul:nth-child(1) > li:nth-child(2)', self.tab)
        male_position = await get_position_by_selector('.VfPpkd-xl07Ob-XxIAqe-OWXEXe-FNFY6c > ul:nth-child(1) > li:nth-child(3)', self.tab)

        if (gender == "male"):
            moveToPoint(male_position.x, male_position.y, 2)
        else:
            moveToPoint(female_position.x, female_position.y, 2)

        pag.click()

        weiter_position = await get_position_by_selector('#birthdaygenderNext', self.tab)
        moveToPoint(weiter_position.x, weiter_position.y, 2)
        pag.click()



class SelectAddressType_routine(Routine):
    async def executeRoutine(self):
        adresse_erstellen_position = await get_position_by_selector_exact('#yDmH0d > c-wiz > div > div.UXFQgc > div > div > div > form > span > section > div > div > div.myYH1.v5IR3e.V9RXW > div.Hy62Fc > div > span > div:nth-child(1) > div > div.uxXgMe > div > div.SCWude', self.tab)
        moveToPoint(adresse_erstellen_position.x + 2, 453, 2)
        pag.click()

        weiter_position = await get_position_by_selector('.VfPpkd-dgl2Hf-ppHlrf-sM5MNb', self.tab)
        moveToPoint(weiter_position.x, weiter_position.y, 2)
        pag.click()
        pauseAt()


class SelectAddress_routine(Routine):
    async def executeRoutine(self):

        #name_field_position = await get_position_by_text('Nutzername', self.tab)
        try:
            name_field_position = await get_position_by_selector('#yDmH0d > c-wiz > div > div.UXFQgc > div > div > div > form > span > section > div > div > div > div.AFTWye > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input', self.tab)
            count = 0
            found_available_name = False

            moveToPoint(name_field_position.x + 20, name_field_position.y + 20, 2)
            pag.click()
            type(generateEmail(name[0], name[1], count))
            pag.press("enter")

            if await is_element_on_page("#passwd", self.tab):
                    print("found password field")
                    found_available_name = True

            while not found_available_name:
                print("looking for available name")
                count = count + 1
                pag.click()
                pag.press("backspace")
                type(str(count))
                pag.press("enter")
                if await is_element_on_page("#passwd", self.tab):
                    found_available_name = True

        except:
            print("did not find address field")
            moveToPoint(993, 451, 2)
            pag.click()
            next_button_position = await get_position_by_selector("#next > div > button > div.VfPpkd-RLmnJb", self.tab)
            moveToPoint(next_button_position.x, next_button_position.y, 2)
            pag.click()
            pauseAt()


class EnterPassword_routine(Routine):
    async def executeRoutine(self):
        password = generate_password(random.randint(8, 15))
        
        password_position = await get_position_by_selector("#passwd", self.tab)
        moveToPoint(password_position.x, password_position.y, 2)
        pag.click()
        type(password)

        confirm_position = await get_position_by_selector("#confirm-passwd", self.tab)
        moveToPoint(confirm_position.x, confirm_position.y, 2)
        pag.click()
        type(password)
        pauseAt()

        weiter_position = await get_position_by_selector("#createpasswordNext", self.tab)
        moveToPoint(weiter_position.x, weiter_position.y, 2)
        pag.click()
        pauseAt()


class EnterPhoneNumber_routine(Routine):
    def __init__(self, tab, country):
        super().__init__(tab)
        self.country = country

    async def executeRoutine(self):
        enter_successfull = False


        number_field_position = await get_position_by_selector("#phoneNumberId", self.tab)
        moveToPoint(number_field_position.x, number_field_position.y, 2)
        pag.click()

        while (enter_successfull == False):
            phone = await getPhoneNumber(self.country)
    
            try:
                type(phone.number)
                length = len(phone.number)
                pag.press("Enter")
            except: 
                print("could not get phone number")
                continue

            try:
                code_field_position = await get_position_by_selector("#code", self.tab)
                print("number available")
            except:
                print("phone number banned")
                cancelled = await cancelOrder(phone.id)
                pag.click()
                for i in range (0, length):
                    pag.press("backspace")
                continue

            start_time = time.time()
            timeout = 30

            while (True):
                code = await checkStatus(phone.id)
                if(code):
                   
                    moveToPoint(code_field_position.x, code_field_position.y, 2)
                    pag.click()
                    type(code)
                    pag.press("Enter")
                    enter_successfull = True
                    break
                
                if time.time() - start_time > timeout:
                    print("Timeout: Code was not received within time limit.")
                    await cancelOrder(phone.id)
                    pag.hotkey('alt', 'left')
                    break





class DeclineRecoveryMailRoutine(Routine):
    async def executeRoutine(self):
        declinemail_position = get_position_by_selector("#recoverySkip > div > button > div.VfPpkd-RLmnJb", self.tab)
        moveToPoint(declinemail_position.x, declinemail_position.y, 2)
        pag.click()












'''
with open (os.path.join(source_dir, "persistentValues\selectAddress.json")) as f:
    data = json.load(f)
if(random.randint(0, 1) == 0):
    moveToPoint(data["firstAddressX"], data["firstAddressY"], 2)
    pag.click()
else: 
    moveToPoint(data["secondAddressX"], data["secondAddressY"], 2)
    pag.click()
    pauseAt()
moveToPoint(data["weiterButtonX"], data["weiterButtonY"], 2)
pauseAt()

'''



