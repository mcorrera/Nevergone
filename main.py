import datetime
import time

from selenium.webdriver.common.by import By

import selensetup
import bs4 as BeautifulSoup
import settings
import prep


def signguestbook(title, OK):
    if OK:
        now = datetime.datetime.now()
        signtime = now.strftime("%m/%d/%Y, %H:%M:%S")
        str = f"{title} was signed on {signtime}\n"
    else:
        str = f"{title} was already signed.\n"

    with open('guestbook.txt', 'a', newline='') as f:
        f.writelines(str)

    print(str)


def login():
    url = "http://www.never-gone.com/"
    username = "Marc Correra"
    myxpath = '//*[@id="top"]/table/tbody/tr[2]/td/div[2]/div/div[1]'

    # testurl = "http://www.never-gone.com/Memorials/Default.aspx?m=mhBfti4Owpt/bwZs6XjW4Q%3d%3d"

    html = prep.getpage(url)
    settings.driver.find_element(By.XPATH, myxpath).click()
    title = settings.driver.title

    # html = prep.getpage(testurl)
    soup = prep.makesoup(html)
    title = settings.driver.title

    if prep.findtext(username):
        # print(f"{username} found")
        signguestbook(title, False)
    else:
        selensetup.scrollwindow()
        id = "ctl00_MemorialSidePanel1_txtSignGuestBook"
        settings.driver.find_element(By.ID, id).send_keys(username)
        time.sleep(10)
        clickid = "ctl00_MemorialSidePanel1_btnSignGuestbook"
        clickname = "ctl00$MemorialSidePanel1$btnSignGuestbook"
        clickcss = "#ctl00_MemorialSidePanel1_btnSignGuestbook"
        clickpath = "//div[6]/table/tbody/tr/td/input"
        button = settings.driver.find_element(By.ID, clickid)
        button.click()
        signguestbook(title, True)


driver = selensetup.initucdriver(False)
settings.init(driver)
for i in range(3):
    login()
settings.end()
# test2
