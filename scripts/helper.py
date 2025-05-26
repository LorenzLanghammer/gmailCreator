import json
import requests
import random
import string
import zendriver as zd
import asyncio
from country_values import *


class Number:
    def __init__(self, id, number):
        self.id = id
        self.number = number

def generateName():
    base_url = "https://randomuser.me/api/"
    response = requests.get(f"{base_url}")
    if response.status_code == 200:
        data = response.json()
        person = data["results"][0]
        firstName = person["name"]["first"]
        lastName = person["name"]["last"]
        gender = person["gender"]
    return firstName, lastName, gender



def generateEmail(firstName, lastName, count):
    count += 1
    return firstName + '.' + lastName + f'{count}'


def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = ".,!?;:-_"

    # Make sure to include at least one from each group
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(punctuation),
    ]


    all_chars = lowercase + uppercase + digits + punctuation
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)
    return ''.join(password)


#asyncio.run(getPhoneNumber())













