import settings
from bs4 import BeautifulSoup
import selensetup

def getpagesource ():
    html = settings.driver.page_source
    return html


def getpage(url):
    settings.driver.get(url)
#    selensetup.randomsleep()
#    html = settings.driver.page_source
    html = getpagesource()
    return html


def remakesoup():
    html = getpagesource()
    page = makesoup(html)
    return page


def makesoup(html):
    page = BeautifulSoup(html, 'lxml')
    return page


def findtext(soup, text):
    #    y = soup.find_all(text=text)
    if len(soup.find_all(text=text)) != 0:
        return True
    else:
        return False


def checkpage(soup):
    errortext = "Correra"
    if findtext(soup, errortext):
        print("Correra Found")
        return False
    else:
        return True
