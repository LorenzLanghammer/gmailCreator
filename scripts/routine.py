import time
import pyautogui as pag
from gui_functions import *
import pyscreeze
from helper import*
import zendriver as zd
import asyncio
#from smsActivate import *
from database.dbInterface import *
from smsProvider import * 
import pyperclip


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

create_gmail_position = {
    "AUSTRIA": {"x": 1424, "y": 441}, 
    "DENMARK": {"x": 1108, "y": 429},
    "POLAND": {"x": 1430, "y": 453},
    "NETHERLANDS": {"x": 1427, "y": 442},
    "SWEDEN": {"x": 1426, "y": 447},
    "ROMANIA": {"x": 1424, "y": 441},
    "ITALY": {"x": 1424, "y": 441},
    "GREECE": {"x": 1424, "y": 441}
}

#name = generateName()
password = ""
country = ""
phone_id = 0
username = ""
number_first_attempt = True

sms_provider_daysisim = DaisySim()
sms_provider_smsactivate = SmsActivate()

sms_provider = DaisySim()

class Routine:
    def __init__(self, tab, identifier):
        self.tab = tab
        self.identifier = identifier
    async def executeRoutine(self):
        pass

class EnterCredentials_routine(Routine):
    def __init__(self, tab, proxy_username, proxy_password):
        super().__init__(tab, identifier="")
        self.proxy_username = proxy_username
        self.proxy_password = proxy_password

    async def executeRoutine(self):
        moveToPoint(917, 222, 2)
        pyautogui.click()
        pyautogui.write(self.proxy_username)

        moveToPoint(969, 285, 2)
        pyautogui.click()
        pyautogui.write(self.proxy_password)
        pyautogui.press("enter")
    
        moveToPoint(954, 339, 2)
        pyautogui.click()

        #moveToPoint(1892, 113, 2)
        moveToPoint(1727, 63, 2)
        pag.click()
        return True

 
class SearchPage_routine(Routine):
    def __init__(self, tab):
        super().__init__(tab, identifier="#L2AGLb")

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
        return True




class GotoPage_routine(Routine):
    def __init__(self, tab):
        super().__init__(tab, identifier = "#page-width-container > div.main-content > article > section > div > div.article-content-container > div > p:nth-child(5) > a")

    async def executeRoutine(self):
        randomMouseMovement(random.uniform(100, 400), random.uniform(100, 500))
        scrollDown(random.randint(5, 8))

        buttonLocation = await get_position_by_selector("#page-width-container > div.main-content > article > section > div > div.article-content-container > div > p:nth-child(5) > a", self.tab)
        moveToPoint(buttonLocation.x, buttonLocation.y, 2)
        pag.click()
        return True




class SelectAccountType_routine(Routine):

    def __init__(self, tab):
        super().__init__(tab, identifier="accounts.google.com/v3/signin/identifier?")
    async def executeRoutine(self):
    
        await asyncio.sleep(1)
    # #yDmH0d > c-wiz > div > div.JYXaTc > div > div.FO2vFd > div > div > div:nth-child(1) > div > button > div.VfPpkd-RLmnJb
        erstellen_position = await get_position_by_selector('#yDmH0d > c-wiz > div > div.JYXaTc > div > div.FO2vFd > div > div > div:nth-child(1) > div > button > div.VfPpkd-RLmnJb', self.tab)
        #erstellen_position = await get_position_by_text('Create account', self.tab)
        moveToPoint(erstellen_position.x, erstellen_position.y, 3)
        pag.click()

        private_nutzung_position = await get_position_by_selector('[jsname="K4r5Ff"]', self.tab)
        moveToPoint(private_nutzung_position.x, private_nutzung_position.y, 3)

        kind_position = await get_position_by_selector('[jsname="IfUHnf"]', self.tab)
        moveToPoint(kind_position.x, kind_position.y, 3)

        arbeit_position = await get_position_by_selector('[jsname="iAUJgf"]', self.tab)
        moveToPoint(arbeit_position.x + random.randint(-30, 30), arbeit_position.y + random.randint(-10, 20), 3)
        moveToPoint(kind_position.x+ random.randint(-30, 30), kind_position.y + random.randint(-10, 10), 3)
        moveToPoint(private_nutzung_position.x + random.randint(-5, 5), private_nutzung_position.y + random.randint(-2, 2), 3)
        pag.click()
        return True



class EnterName_routine(Routine):

    def __init__(self, tab, first_name, last_name):
        super().__init__(tab, identifier="signup/name")
        self.first_name = first_name
        self.last_name = last_name

    async def executeRoutine(self):

        #firstName = name[0]
        #lastName = name[1]

        first_name_position = await get_position_by_selector("#firstName", self.tab)
        moveToPoint(first_name_position.x + random.randint(-20, 20), first_name_position.y + random.randint(-5, 5), 2)
        pag.click()
        type(self.first_name)
        #type("test")

        last_name_position = await get_position_by_selector("#lastName", self.tab)
        moveToPoint(last_name_position.x + random.randint(-20, 20), last_name_position.y + random.randint(-5, 5), 2)
        pag.click()
        type(self.last_name)
        #type("test")

        weiter_button_position = await get_position_by_selector('[jsname="V67aGc"]', self.tab)
        moveToPoint(weiter_button_position.x + random.randint(-20, 0), weiter_button_position.y + random.randint(-5, 5), 2)
        pag.click()
        return True



class EnterDateAndGender_routine(Routine):

    def __init__(self, tab, gender):
        super().__init__(tab, identifier="signup/birthdaygender")
        self.gender = gender

    async def executeRoutine(self):

        #gender = name[2]
        month = random.randint(1, 12)
        day = random.randint(1, month_days[month])
        year = random.randint(1970, 2004)


        day_position = await get_position_by_selector("#day", self.tab)
        moveToPoint(day_position.x + random.randint(-10, 10), day_position.y+ random.randint(-5, 5), 2)
        pag.click()
        pauseAt()
        type(f'{day}')
        pauseAt()

        month_position = await get_position_by_selector(".VfPpkd-aPP78e", self.tab)
        moveToPoint(month_position.x + random.randint(-5, 5), month_position.y + random.randint(-5, 5), 2)
        pag.click()
        january_position = await get_position_by_selector('.VfPpkd-xl07Ob-XxIAqe-OWXEXe-FNFY6c > ul:nth-child(1) > li:nth-child(2)', self.tab)
        moveToPoint(january_position.x + random.randint(-5, 5), january_position.y + random.randint(-2, 2), 2)

        if month >= 11:
            scrollDown(3)

        selected_month_position = await get_position_by_selector(f'.VfPpkd-xl07Ob-XxIAqe-OWXEXe-FNFY6c > ul:nth-child(1) > li:nth-child({month + 1})', self.tab)
        moveToPoint(selected_month_position.x, selected_month_position.y, 2)
        pag.click()

        year_position = await get_position_by_selector('#year', self.tab)
        moveToPoint(year_position.x + random.randint(-10, 10), year_position.y + random.randint(-5, 5), 2)
        pag.click()
        pauseAt()
        type(f'{year}')
        
        gender_position = await get_position_by_selector('#gender', self.tab)
        moveToPoint(gender_position.x + random.randint(-10, 10), gender_position.y + random.randint(-5, 5), 2)
        pag.click()

        female_position = await get_position_by_selector('.VfPpkd-xl07Ob-XxIAqe-OWXEXe-FNFY6c > ul:nth-child(1) > li:nth-child(2)', self.tab)
        male_position = await get_position_by_selector('.VfPpkd-xl07Ob-XxIAqe-OWXEXe-FNFY6c > ul:nth-child(1) > li:nth-child(3)', self.tab)

        if (self.gender == "male"):
            moveToPoint(male_position.x + random.randint(-5, 5), male_position.y + random.randint(-5, 5), 2)
        else:
            moveToPoint(female_position.x + random.randint(-5, 5), female_position.y + random.randint(-5, 5), 2)

        pag.click()

        weiter_position = await get_position_by_selector('#birthdaygenderNext', self.tab)
        moveToPoint(weiter_position.x + random.randint(-20, 0), weiter_position.y + random.randint(-5, 5), 2)
        pag.click()
        return True



class SelectAddressType_routine(Routine):
    def __init__(self, tab, country):
        super().__init__(tab, identifier="/signup/selectidentifiertype")
        self.country = country

    async def executeRoutine(self):
        #adresse_erstellen_position = await get_position_by_selector_exact('#yDmH0d > c-wiz > div > div.UXFQgc > div > div > div > form > span > section > div > div > div.myYH1.v5IR3e.V9RXW > div.Hy62Fc > div > span > div:nth-child(1) > div > div.uxXgMe > div > div.SCWude', self.tab)
        #moveToPoint(adresse_erstellen_position.x + 2, 453, 2)
        create_position = create_gmail_position[self.country]

        moveToPoint(create_position["x"], create_position["y"], 2)
        pag.click()

        weiter_position = await get_position_by_selector('#yDmH0d > c-wiz > div > div.JYXaTc > div > div > div > div > button > span', self.tab)
        moveToPoint(weiter_position.x - random.randint(0, 30), weiter_position.y + random.randint(-5, 5), 2)
        pag.click()
        pauseAt()
        global country
        country = self.country
        return True



class SelectAddress_routine(Routine):

    def __init__(self, tab, first_name, last_name):
        super().__init__(tab, identifier="signup/username")
        self.first_name = first_name
        self.last_name = last_name

    async def executeRoutine(self):

        #name_field_position = await get_position_by_text('Nutzername', self.tab)
        try:
            name_field_position = await get_position_by_selector('#yDmH0d > c-wiz > div > div.UXFQgc > div > div > div > form > span > section > div > div > div > div.AFTWye > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input', self.tab)
            count = 0
            found_available_name = False

            moveToPoint(name_field_position.x +  20 + random.randint(-30, 30), name_field_position.y + 20 + random.randint(-5, 5), 2)
            pag.click()
            email = generateEmail(self.first_name, self.last_name[1], count)
            type(email)
            #global username
            #username = email
            pag.press("enter")

            if await is_element_on_page("#passwd", self.tab):
                    print("found password field")
                    global username
                    username = email
                    found_available_name = True

            while not found_available_name:
                print("looking for available name")
                count = count + 1
                pag.click()
                pag.press("backspace")
                type(str(count))
                pag.press("enter")
                if await is_element_on_page("#passwd", self.tab):
                    username = email
                    found_available_name = True

        except:
            print("did not find address field")
            moveToPoint(987, 564, 2)
            pag.click()
            asyncio.sleep(1)

            count = 0
            found_available_name = False
            email = generateEmail(self.first_name, self.last_name, count)
            type(email)
            pag.press("enter")

            if await is_element_on_page("#passwd", self.tab):
                    #username = email
                    print("found password field")
                    username = email
                    found_available_name = True

            while not found_available_name:
                print("looking for available name")
                count = count + 1
                pag.click()
                pag.press("backspace")
                type(str(count))
                pag.press("enter")
                if await is_element_on_page("#passwd", self.tab):
                    username = email
                    found_available_name = True
        return True
        
            
           


class EnterPassword_routine(Routine):

    def __init__(self, tab):
        super().__init__(tab, identifier="signup/password")

    async def executeRoutine(self):
        global password
        password = generate_password(random.randint(8, 15))
        
        password_position = await get_position_by_selector("#passwd", self.tab)
        moveToPoint(password_position.x + - 250 + random.randint(-30, 30), password_position.y + random.randint(-5, 5) - 5, 2)
        pag.click()
        type(password)

        confirm_position = await get_position_by_selector("#confirm-passwd", self.tab)
        moveToPoint(confirm_position.x + random.randint(-30, 30), confirm_position.y + random.randint(-5, 5), 2)
        pag.click()
        type(password)
        pauseAt()

        weiter_position = await get_position_by_selector("#createpasswordNext", self.tab)
        moveToPoint(weiter_position.x + random.randint(-20, 0), weiter_position.y + random.randint(-5, 5), 2)
        pag.click()
        pauseAt()
        return True


phone_id = 0

class EnterPhoneNumber_routine(Routine):
    def __init__(self, tab, country, browser):
        super().__init__(tab, identifier="signup/startmtsmsidv")
        self.country = country
        self.browser = browser

    async def executeRoutine(self):
        number_field_position = await get_position_by_selector("#phoneNumberId", self.tab)
        moveToPoint(number_field_position.x + random.randint(-30, 30), number_field_position.y + random.randint(-3, 3), 2)
        pag.click()

        global number_first_attempt
        if not number_first_attempt:
            print("first attempt true")
            for i in range(0, 12):
                print("removing character")
                pag.press("backspace")
        else:
            number_first_attempt = False
            print("first attempt set to")


        enter_successfull = False
        number_field_position = await get_position_by_selector("#phoneNumberId", self.tab)
        moveToPoint(number_field_position.x + random.randint(-30, 30), number_field_position.y + random.randint(-3, 3), 2)
        pag.click()


        while (enter_successfull == False):
            phone = await sms_provider.getPhoneNumber(self.country)
            #phone = await getPhoneNumber(self.browser, self.tab)
    
            try:
                #type(phone.number)
                pyperclip.copy(phone.number)
                pyautogui.hotkey("ctrl", "v")
                length = len(phone.number)
                global phone_id
                phone_id = phone.id
                pag.press("Enter")
            except: 
                print("could not get phone number")
                continue
            
            if await is_element_on_page("#code", self.tab):
                print("number available")
                enter_successfull = True
            else:
                print ("number banned")
                cancelled = await sms_provider.cancelOrder(phone_id)
                pag.click()
                for i in range (0, length + 1):
                    pag.press("backspace")
                continue
        return True
        




class EnterCodeRoutine(Routine):
    def __init__(self, tab):
        super().__init__(tab, identifier="verifyphone")
    
    async def executeRoutine(self):
        start_time = time.time()
        timeout = 30

        while (True):
            code = await sms_provider.checkStatus(phone_id)
            print(phone_id)
            if(code):
                code_field_position = await get_position_by_selector("#code", self.tab)
                moveToPoint(code_field_position.x + random.randint(-10, 10), code_field_position.y + random.randint(-3, 3), 2)
                pag.click()
                type(code)
                pag.press("Enter")
                break
            
            if time.time() - start_time > timeout:
                print("Timeout: Code was not received within time limit.")
                await sms_provider.cancelOrder(phone_id)
                pag.hotkey('alt', 'left')
                global number_first_attempt
                number_first_attempt = False
                break
        return True
        




class DeclineRecoveryMailRoutine(Routine):
    def __init__(self, tab):
        super().__init__(tab, identifier="addrecoveryemail")

    async def executeRoutine(self):
        declinemail_position = await get_position_by_selector("#recoverySkip > div > button", self.tab)
        moveToPoint(declinemail_position.x + random.randint(-5, 5), declinemail_position.y + random.randint(-3, 3), 2)
        pag.click()
        return True


class DeclineRecoveryPhoneRoutine(Routine):
    def __init__(self, tab):
        super().__init__(tab, identifier="signup/webaddrecoveryphone")
    
    async def executeRoutine(self):
        next_button_position = await get_position_by_selector("#recoveryNext > div > button > div.VfPpkd-RLmnJb", self.tab)
        moveToPoint(next_button_position.x + random.randint(-20, 0), next_button_position.y + random.randint(-3, 3), 2)
        pag.click()
        await asyncio.sleep(3)
        return True


class DeclinePhoneUsageRoutine(Routine):
    def __init__(self, tab):
        super().__init__(tab, identifier="webphoneusage")

    async def executeRoutine(self):
        decline_button = await get_position_by_selector("#yDmH0d > c-wiz > div > div.JYXaTc.F8PBrb > div > div.TNTaPb > div:nth-child(2) > div > div > button > div.VfPpkd-RLmnJb", self.tab)
        moveToPoint(decline_button.x + random.randint(-10, 0), decline_button.y + random.randint(-3, 3), 2)
        pag.click()
        await asyncio.sleep(3)
        return True


class ConfirmAccountCreationRoutine(Routine):
    def __init__(self, tab):
        super().__init__(tab, identifier="confirmation")
    async def executeRoutine(self):
        next_position = await get_position_by_selector("#yDmH0d > c-wiz > div > div.JYXaTc > div > div > div > div > button > span", self.tab)
        moveToPoint(next_position.x, next_position.y, 2)
        pag.click()
        return True




class Personalization(Routine):
    def __init__(self, tab):
        super().__init__(tab, identifier="personalizationchoice")

    async def executeRoutine(self):
        moveToPoint(996, 431, 2)
        pag.click()
        #one_step_position = await get_position_by_selector("#yDmH0d > c-wiz > div > div.UXFQgc > div > div > div.AcKKx > form > span > section > div > div > div > div > div.Hy62Fc > div > span > div:nth-child(1) > div > div.uxXgMe > div > div.SCWude > div", self.tab)
        next_button_position = await get_position_by_selector("#yDmH0d > c-wiz > div > div.JYXaTc > div > div > div > div > button > div.VfPpkd-RLmnJb", self.tab)
        moveToPoint(next_button_position.x, next_button_position.y, 2)
        pag.click()
        return True


class ExpressSettingsRoutine(Routine):
    def __init__(self, tab):
        super().__init__(tab, identifier="expresssettings")
    async def executeRoutine(self):
        scrollDown(15)
        accept_all_position = await get_position_by_selector("#yDmH0d > c-wiz > div > div.JYXaTc.COi2Ke.N0osAb.F8PBrb.lUWEgd.NNItQ > div > div.TNTaPb > div:nth-child(1) > div > div > button > div.VfPpkd-RLmnJb", self.tab)
        moveToPoint(accept_all_position.x, accept_all_position.y, 2)
        pag.click()
        return True
        
class ConfirmSettingsRoutine(Routine):
    def __init__(self, tab):
        super().__init__(tab, identifier="confirmpersonalizationsettings")
    
    async def executeRoutine(self):
        scrollDown(15)
        confirm_position = await get_position_by_selector("#yDmH0d > c-wiz > div > div.JYXaTc.F8PBrb > div > div > div:nth-child(2) > div > div > button > div.VfPpkd-RLmnJb", self.tab)
        moveToPoint(confirm_position.x, confirm_position.y, 2)
        pag.click()
        return True

class AgreeTosRoutine(Routine):
    def __init__(self, tab):
        super().__init__(tab, identifier="termsofservice")
    
    async def executeRoutine(self):
        scrollDown(15)
        agree_position = await get_position_by_selector("#yDmH0d > c-wiz > div > div.JYXaTc.lUWEgd > div > div.TNTaPb > div > div > button > div.VfPpkd-RLmnJb", self.tab)
        moveToPoint(agree_position.x, agree_position.y, 2)
        pag.click()
        return True

class SaveProfileRoutine(Routine):
    def __init__(self, tab, username):
        super().__init__(tab, identifier="utm_source=sign_in_no_continue")
        self.username = username

    async def executeRoutine(self):
        addProfile(username, password, country)
        await self.tab.send(zd.cdp.target.close_target(self.tab.target.target_id))
        return False









