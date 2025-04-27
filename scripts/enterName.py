import requests
import random

base_url = "https://randomuser.me/api/"
response = requests.get(f"{base_url}")

timeOffsetLowerBound = 0.003648996353149414
timeOffsetUpperBound = 0.08896112442016602


def generateName():
    if response.status_code == 200:
        data = response.json()
        person = data["results"][0]
        firstName = person["name"]["first"]
        lastName = person["name"]["last"]
    return firstName, lastName

def generateTimeOffset():
    return random.uniform(timeOffsetLowerBound, timeOffsetUpperBound)


def generateTextInsertion(text):
    events = []
    for char in text:
        event = f'{{"type":"keyboardEvent","key":"{char}","timestamp":{generateTimeOffset()},"pressed":true}}, \n'
        events.append(event)
        event = f'{{"type":"keyboardEvent","key":"{char}","timestamp":{generateTimeOffset()},"pressed":false}}, \n'
        events.append(event)
    return events


