import random
import time

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

global driver


def end():
    global driver
    driver.quit()


def randomsleep():
    delaytime = random.randrange(5, 10)
    time.sleep(delaytime)


def getoptions():
    myoptions = Options()
    myoptions.add_argument("--incognito")
    return myoptions


def scrollwindow():
    driver.execute_script("window.scrollTo(0, 1500)")
    time.sleep(2)


def waitforit(csstoget):
    try:
        element = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, csstoget)))
        #       print(f"{csstoget} was FOUND!")
        time.sleep(1)
        return True
    except:
        print(f"{csstoget} was not found.")
        return False


def initucdriver(proxies):
    global driver
    options = uc.ChromeOptions()
    if proxies:
        PROXY = "46.4.73.88:2000"  # IP:PORT or HOST:PORT
        options.add_argument('--proxy-server=%s' % PROXY)
    options.headless = False
    driver = uc.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


def initchromedriver(self):
    global driver
    chrome_path = "/Drivers/chromedriver.exe"
    myoptions = getoptions()
    s = Service(r"/Drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=myoptions)
    driver.maximize_window()
    return driver
