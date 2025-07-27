from enum import Enum
import json

class CountryCode(Enum):
    AUSTRIA = "+43"
    BELGIUM = "+32"
    CANADAVANCOUVER = "+1"
    CROATIA = "+385"
    CYPRUS = "+357"
    CZECH = "+420"
    DENMARK = "+45"
    ENGLAND = "+44"
    FINLAND = "+358"
    FRANCE = "+33"
    GERMANY = "+49"
    GREECE = "+30"
    HUNGARY = "+36"
    IRELAND = "+353"
    ITALY = "+39"
    ISRAEL = "+972"
    LATVIA = "+371"
    LITHUANIA = "+370"
    NETHERLANDS = "+31"
    NORWAY = "+47"
    POLAND = "+48"
    PORTUGAL = "+351"
    ROMANIA = "+40"
    RUSSIA = "+7"
    SERBIA = "+381"
    SLOVAKIA = "+421"
    SLOVENIA = "+386"
    SPAIN = "+34"
    SWEDEN = "+46"
    SOUTH_AFRICA = "+27"
    SWITZERLAND = "+41"
    THAILAND = "+66"
    TURKEY = "+90"
    UZBEKISTAN = "+998"
    USA = "+1"


class Language(Enum):
    AUSTRIA = "de-AT"
    BELGIUM = "nl-BE"
    CANADAVANCOUVER = "en-CA"
    CROATIA = "hr-HR"
    CYPRUS = "el-CY"
    CZECH = "cs-CZ"
    DENMARK = "da-DK"
    ENGLAND = "en-GB"
    FINLAND = "fi-FI"
    FRANCE = "fr-FR"
    GERMANY = "de-DE"
    GREECE = "el-GR"
    HUNGARY = "hu-HU"
    IRELAND = "en-IE"
    ITALY = "it-IT"
    ISRAEL = "he-IL"
    LATVIA = "lv-LV"
    LITHUANIA = "lt-LT"
    NETHERLANDS = "nl-NL"
    NORWAY = "no-NO"
    POLAND = "pl-PL"
    PORTUGAL = "pt-PT"
    ROMANIA = "ro-RO"
    RUSSIA = "ru-RU"
    SLOVAKIA = "sk-SK"
    SLOVENIA = "sl-SI"
    SPAIN = "es-ES"
    SERBIA = "sr-RS"
    SWEDEN = "sv-SE"
    SWITZERLAND = "de-CH"
    SOUTH_AFRICA = "en-ZA"
    CANADA = "en-CA"
    THAILAND= "th-TH"
    TURKEY = "tr-TR"
    UZBEKISTAN = "uz-UZ"
    USA = "en-US"
    


class Country(Enum):
    AUSTRIA = "austria"
    BELGIUM = "belgium"
    CROATIA = "croatia"
    CYPRUS = "cyprus"
    CZECH = "czech"
    DENMARK = "denmark"
    ENGLAND = "england"
    FINLAND = "finland"
    FRANCE = "france"
    GERMANY = "germany"
    GREECE = "greece"
    HUNGARY = "hungary"
    IRELAND = "ireland"
    ITALY = "italy"
    ISRAEL = "israel"
    LATVIA = "latvia"
    LITHUANIA = "lithuania"
    NETHERLANDS = "netherlands"
    NORWAY = "norway"
    POLAND = "poland"
    ROMANIA = "romania"
    RUSSIA = "russia"
    SLOVAKIA = "slovakia"
    SLOVENIA = "slovenia"
    SOUTH_AFRICA = "south_africa"
    SPAIN = "spain"
    SERBIA = "serbia"
    SWEDEN = "sweden"
    SWITZERLAND = "switzerland"
    USA = "usa"



class CountryTimezone(Enum):
    AUSTRIA = "Europe/Vienna"
    BELGIUM = "Europe/Brussels"
    CANADAVANCOUVER = "America/Vancouver"
    CROATIA = "Europe/Zagreb"
    CYPRUS = "Asia/Nicosia"  # Not Europe/, but correct for Cyprus
    CZECH = "Europe/Prague"
    DENMARK = "Europe/Copenhagen"
    ENGLAND = "Europe/London"
    FINLAND = "Europe/Helsinki"
    FRANCE = "Europe/Paris"
    GERMANY = "Europe/Berlin"
    GREECE = "Europe/Athens"
    HUNGARY = "Europe/Budapest"
    IRELAND = "Europe/Dublin"
    ITALY = "Europe/Rome"
    ISRAEL = "Asia/Jerusalem"
    LATVIA = "Europe/Riga"
    LITHUANIA = "Europe/Vilnius"
    NETHERLANDS = "Europe/Amsterdam"
    NORWAY = "Europe/Oslo"
    POLAND = "Europe/Warsaw"
    ROMANIA = "Europe/Bucharest"
    RUSSIA = "Europe/Moscow"
    SLOVAKIA = "Europe/Bratislava"
    SLOVENIA = "Europe/Ljubljana"
    SPAIN = "Europe/Madrid"
    SERBIA = "Europe/Belgrade"
    SWEDEN = "Europe/Stockholm"
    SOUTH_AFRICA = "Africa/Johannesburg"
    SWITZERLAND = "Europe/Zurich"
    THAILAND = "Asia/Bangkok"
    TURKEY = "Europe/Istanbul"
    UZBEKISTAN = "Asia/Tashkent"
    USA = "America/New_York"


class TimeOffset(Enum):
    AUSTRIA = +120
    ENGLAND = 60
    GERMANY = 120 
    GREECE = 180
    ISRAEL = 180
    ITALY = +120
    POLAND = 120
    ROMANIA = -180
    RUSSIA = 180
    SWEDEN = -120   
    TURKEY = 180  
    UZBEKISTAN = 300
    USA = -240
    SERBIA = 120
    SOUTH_AFRICA = +120
 
    



class CountryProxy(Enum):
    AUSTRIA = "at"
    BELGIUM = "be"
    CANADAVANCOUVER = "ca"
    COLOMBIA = "co"
    CROATIA = "hr"
    CYPRUS = "cy" 
    CZECH = "cz"
    DENMARK = "dk"
    ENGLAND = "gb"
    FINLAND = "fi"
    FRANCE = "fr"
    GERMANY = "de"
    GREECE = "gr"
    HUNGARY = "hu"
    IRELAND = "ie"
    ITALY = "it"
    ISRAEL = "il"
    LATVIA = "lv"
    LITHUANIA = "lt"
    NETHERLANDS = "nl"
    NORWAY = "no"
    POLAND = "pl"
    ROMANIA = "ro"
    RUSSIA = "ru"
    SLOVAKIA = "sk"
    SLOVENIA = "si"
    SPAIN = "es"
    SERBIA = "rs"
    SWEDEN = "se"
    SWITZERLAND = "ch"
    THAILAND = "th"
    TURKEY = "tr"
    UZBEKISTAN = "uz"
    USA = "us"
    SOUTH_AFRICA = "za"

class CountryNumber(Enum):
    AUSTRIA = 50
    SWEDEN = 46
    POLAND = 15
    CANADAVANCOUVER = 36
    ENGLAND = 16
    ITALY = 86
    ISRAEL = 13
    THAILAND = 52
    COLOMBIA = 33
    TURKEY = 62
    UZBEKISTAN = 40
    USA = 187
    GREECE = 129
    ROMANIA = 32   
    RUSSIA = 0
    SERBIA = 29
    SOUTH_AFRICA = 31


class CountryLanguageHeaders(Enum):
    AUSTRIA = "de-AT,de;q=0.9,en-US;q=0.8,en;q=0.7"
    CANADAVANCOUVER = "en-CA,en;q=0.9,en-US;q=0.8,fr;q=0.7"
    ENGLAND = "en-GB,en;q=0.9"
    FRANCE = "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
    GERMANY = "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
    GREECE = "el-GR,el;q=0.9,en-US;q=0.8,en;q=0.7"
    ROMANIA = "ro-RO,ro;q=0.9,en-US;q=0.8,en;q=0.7"
    RUSSIA = "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
    CYPRUS = "el-GR,el;q=0.9,en-US;q=0.8,en;q=0.7"
    NETHERLANDS = "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7"
    SWEDEN = "sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7"
    SOUTH_AFRICA = "en-ZA,en;q=0.9"
    SERBIA = "sr-RS,sr;q=0.9,en-US;q=0.8,en;q=0.7"
    DENMARK = "da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7"
    CANADA = "en-CA,fr-CA;q=0.9,en;q=0.8,fr;q=0.7"
    PORTUGAL = "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7"
    ITALY = "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7"
    ISRAEL = "Accept-Language: he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7"
    POLAND = "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"
    THAILAND = "th-TH,th;q=0.9,en-US;q=0.8,en;q=0.7"
    COLOMBIA = "es-CO,es;q=0.9,en-US;q=0.8,en;q=0.7"
    TURKEY = "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
    UZBEKISTAN = "uz-UZ,uz;q=0.9,ru;q=0.8,en-US;q=0.7,en;q=0.6"
    USA = "en-US,en;q=0.9"




