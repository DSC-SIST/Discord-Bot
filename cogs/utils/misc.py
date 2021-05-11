# Built-In Libraries/Modules/Packages
from json import loads
from re import findall

# Third Party Libraries/Modules/Packages
from urllib.request import urlopen
from pysafebrowsing import SafeBrowsing

# User Defined Libraries/Modules/Packages
from .settings import Settings


def checklinkfunc(link):
    """
    A user defined function that uses the Google's Safe
    Browsing API to check whether a given link is malicous
    or not.
    """

    key = Settings().SECRETS['GOOGLE_SAFE_BROWSING_API_KEY']
    checker = SafeBrowsing(f"{key}")
    regex = r"{regex}".format(regex=Settings().SECRETS['VALID_LINK_REGEX'])
    url = findall(regex, link)

    try:
        link = url[0][0]
        response = checker.lookup_urls([link])
        if response[link]["malicious"] == False:
            return "{link} **is safe!**".format(link=link)
        elif response[link]["malicious"] == True:
            return "{link} **is malicious!!!**".format(link=link)
        else:
            return "Something's wrong"
    except:
        message = "There was no link in your command\n"
        message += "Example command: ``checklink <pastethelinkhere>``"
        return message


def getJoke():
    url = Settings().SECRETS["JOKE_API"]
    response = urlopen(url)
    data = response.read()
    jsonData = loads(data)
    return {
        "setup": str(jsonData[0]['setup']).capitalize(),
        "punchline": str(jsonData[0]['punchline']).capitalize()
    }
