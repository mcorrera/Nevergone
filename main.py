import time

from selenium.webdriver.common.by import By

import selensetup
import bs4 as BeautifulSoup
import settings
import prep


def processmainpage(url):
    inner = "css-1x3b5qq"
    outer = "product-tile css-1iewwf2-TileWrapper"

    html = prep.getpage(url)
    soup = prep.makesoup(html)
    numnewitems = 0
    for item in soup.find_all(class_=outer):
        new_item = settings.StockxItem()
        new_item.url = "https://stockx.com" + item.find('a')['href']
        new_item.name = item.find(class_=inner).text
        numnewitems += 1
        settings.Items.append(new_item)
    return numnewitems


def login():
    url = "http://www.never-gone.com/"
    html = prep.getpage(url)
    soup = prep.makesoup(html)
    username = "Marc Correra"
    password = "Lindo123$"
    if prep.checkpage(soup):
        myxpath = '//*[@id="top"]/table/tbody/tr[2]/td/div[2]/div/div[1]'
        settings.driver.find_element(By.XPATH, myxpath).click()
        selensetup.scrollwindow()
        id = "ctl00_MemorialSidePanel1_txtSignGuestBook"
        settings.driver.find_element(By.ID, id).send_keys(username)
        time.sleep(10)
        clickid = "ctl00_MemorialSidePanel1_btnSignGuestbook"
        clickname = "ctl00$MemorialSidePanel1$btnSignGuestbook"
        clickcss = "#ctl00_MemorialSidePanel1_btnSignGuestbook"
        clickpath = "//div[6]/table/tbody/tr/td/input"
#        button = settings.driver.find_element(By.XPATH, clickpath)
        button = settings.driver.find_element(By.ID, clickid)
        button.click()
        print("Signed")


driver = selensetup.initucdriver(False)
settings.init(driver)
for i in range(4):
    login()
settings.end()
