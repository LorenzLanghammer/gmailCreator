
import pyautogui as pag
import sys
import os


script_dir = os.path.dirname(os.path.abspath(__file__))         # project/folder
scripts_dir = os.path.abspath(os.path.join(script_dir, "..", "scripts"))  # project/scripts
sys.path.append(scripts_dir)
from database.dbInterface import *
from routine import *

class AcceptCookiesRoutine(Routine):
    def __init__(self, tab):
        super().__init__(tab, identifier="")

    async def executeRoutine(self):
        moveToPoint(1089, 831, 2)
        pag.click()


class EnterPersonalInfosRoutine(Routine):
    def __init__(self, tab, first_name, last_name, gender):
        super().__init__(tab, identifier="https://www.facebook.com/reg/")
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
    

    async def executeRoutine(self):
        first_name_position = await get_position_by_text("Vorname", self.tab)
        moveToPoint(first_name_position.x, first_name_position.y, 2)
        pag.click()
        type(self.first_name)

        last_name_position =await get_position_by_text("Nachname", self.tab)
        moveToPoint(last_name_position.x, last_name_position.y, 2)
        pag.click()
        type(self.last_name)

        days_position = await get_position_by_selector("#day", self.tab)
        moveToPoint(days_position.x, days_position.y, 2)
        pag.click()
        moveToPoint(812, random.randint(415, 887), 2)
        pag.click()
        
        month_position = await get_position_by_selector("#month", self.tab)
        moveToPoint(month_position.x, month_position.y, 2)
        pag.click()
        moveToPoint(930, random.randint(420, 691), 2)
        pag.click()
        
        year_position = await get_position_by_selector("#year", self.tab)
        moveToPoint(year_position.x, year_position.y, 2)
        pag.click()
        moveToPoint(year_position.x, 421, 2)
        scrollDown(3)
        moveToPoint(year_position.x, random.randint(421, 894), 2)
        pag.click()

        if (self.gender == "female"):
            female_position = await get_position_by_text("Weiblich", self.tab)
            moveToPoint(female_position.x, female_position.y, 2)
            #moveToPoint(806, 455, 2)
            pag.click()
        else:
            male_position = await get_position_by_text("Männlich", self.tab)
            moveToPoint(male_position.x, male_position.y, 2)
            pag.click()

        verification_email = get_email_fb()[1]
        email_position = await get_position_by_text("Handynummer oder E-Mail-Adresse", self.tab)
        moveToPoint(email_position.x, email_position.y, 2)
        pag.click()
        type(verification_email)

        password_position = await get_position_by_text("Neues Passwort", self.tab)
        moveToPoint(password_position.x, password_position.y, 2)
        pag.click()
        type(generate_password())

        register_position = await get_position_by_text("Registrieren", self.tab)
        moveToPoint(register_position.x, register_position.y, 2)
        pag.click()


