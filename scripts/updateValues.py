import json
import os

source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


searchPageValues = {
    "google_resultX": 292,
    "google_resultY": 383
}



selectAccountTypeValues = {
    "erstellenX": 1252,
    "erstellenY": 692,
    "privateNutzungX": 1293,
    "privateNutzungY": 744,
    "kindX": 1317,
    "kindY": 774,
    "arbeitX": 1341, 
    "arbeitY": 838
}


enterNameValues = {
    "firstNameX": 1183,
    "firstNameY": 479,
    "lastNameX": 1080, 
    "lastNameY": 554,
    "weiterButtonX": 1420,
    "weiterButtonY": 660,
}


enterDateAndGenderValues = {
    "tagX": 1050,
    "tagY": 467,
    "monatX":1228,
    "monatY":461,
    "jahrX": 1386,
    "jahrY": 470,
    "genderX": 1161,
    "genderY": 545,
    "maleX": 1128,
    "maleY": 617,
    "femaleX": 1170,
    "femaleY": 579,
    "weiterButtonX": 1420,
    "weiterButtonY": 660
}

selectAddressTypeValues = {
    "adresseErstellenX": 1455,
    "adresseErstellenY": 440,
    "weiterButtonX": 1428,
    "weiterButtonY": 688
}
    #"gmailErstellenX": 1457,
    #"gmailErstellenY": 445,


selectAddressValues = {
    "firstAddressX": 1020,
    "firstAddressY": 456,
    "secondAddressX": 1022,
    "secondAddressY": 515,
    "weiterButtonX": 1427, 
    "weiterButtonY": 674
}





def updateValues():
    with open (os.path.join(source_dir, "persistentValues\searchPage.json"), "w") as f:
        json.dump(searchPageValues, f)
    with open (os.path.join(source_dir, "persistentValues\selectAccountType.json"), "w") as f:
        json.dump(selectAccountTypeValues, f)
    with open (os.path.join(source_dir, "persistentValues\enterName.json"), "w") as f:
        json.dump(enterNameValues, f)
    with open (os.path.join(source_dir, "persistentValues\enterDateAndGender.json"), "w") as f: 
        json.dump(enterDateAndGenderValues, f)
    with open (os.path.join(source_dir, "persistentValues\selectAddressType.json"), "w") as f:
        json.dump(selectAddressTypeValues, f)
    with open (os.path.join(source_dir, "persistentValues\selectAddress.json"), "w") as f:
        json.dump(selectAddressValues, f)


updateValues()



