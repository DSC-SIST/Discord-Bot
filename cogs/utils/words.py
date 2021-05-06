# Built-In Libraries/Modules/Packages
from json import loads
import time

# Third Party Libraries/Modules/Packages
import requests
from urllib.parse import urlencode
from urllib.request import urlopen

# User Defined Libraries/Modules/Packages
from .settings import Settings

def getWordOfTheDay():
    WOTD_API_URL = Settings().SECRETS['WOTD_API_URL']

    url_args = {
        'date': time.strftime('%Y-%m-%d'),
        'api_key': str(Settings().SECRETS['WOTD_API_KEY'])
    }

    url = WOTD_API_URL + "{}".format(urlencode(url_args))
    response = urlopen(url)
    data = response.read()
    jsonData = loads(data)

    return {
        "word": str(jsonData['word']).capitalize(),
        "meaning": str(jsonData['definitions'][0]['text'])
    }
