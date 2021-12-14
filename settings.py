global Items
global StockxItem
global driver


def init(webdriver):
    global driver
    driver = webdriver


def zeroitems():
    global Items
    Items = []


def end():
    global driver
    driver.quit()


class Item:
    def __init__(self):
        self.name = ""
        self.url = ""
