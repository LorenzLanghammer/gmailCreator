import json
import os

source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

enterNameValues = {
    "firstNameX": 1183,
    "firstNameY": 479,
    "lastNameX": 1080, 
    "lastNameY": 554
}

openPageValues = {
    "google_resultX": 292,
    "google_resultY": 383,
    "num_scrolls": 5,
    "createX": 268,
    "createY": 608,
    "erstellenX": 1252,
    "erstellenY": 692,
    "privateNutzungX": 1293,
    "privateNutzungY": 744
}

def updateEnterNameValues():
    with open (os.path.join(source_dir, "persistentValues\enterName.json"), "w") as f:
        json.dump(enterNameValues, f)


def updateEnterNameValues():
    with open (os.path.join(source_dir, "persistentValues\openPage.json"), "w") as f:
        json.dump(openPageValues, f)


updateEnterNameValues()



