import json
import requests

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
