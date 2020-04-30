#!C:\Python34 python

from sendmail import SendMail

#Importing packages
import config

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options


class Bjs:
    def __init__(self):

        self.productList = [ 'https://www.bjs.com/product/gold-medal-premium-quality-all-purpose-flour-2-pk10-lbs/3000000000000139631',
                            'https://www.bjs.com/product/fleischmanns-instant-dry-yeast-2-pk1-lb/3000000000000222175',
                            'https://www.bjs.com/product/lysol-lemon-all-purpose-cleaner-32-oz-spray-bottle-with-144-oz-refill/3000000000000732604',
                            'https://www.bjs.com/product/lysol-disinfectant-spray-4-ct19-oz/3000000000000147813',
                            'https://www.bjs.com/product/scott-1100-sheets-1-ply-bath-tissue-36-pk/3000000000000190611',
                            'https://www.bjs.com/product/berkley-jensen-160-sheet-choose-a-size-paper-towels-12-pk/3000000000000191927',
                            'https://www.bjs.com/product/berkley-jensen-full-sheet-white-paper-towels-12-pk/3000000000000183381',
                            'https://www.bjs.com/product/bounty-essentials-select-a-size-double-roll-paper-towels-12-pk---white/3000000000001232799',
                            'https://www.bjs.com/product/berkley-jensen-ultra-strong-bath-tissue-24-ct/3000000000001957283',
                            'https://www.bjs.com/product/berkley-jensen-ultra-soft-bath-tissue-24-ct/3000000000001957281'
                            ]



        self.baseurl = ''
        self.numberOfMinutes = 1
        self.arr = ['ADD TO CART']
        self.title = ""

    def readBjs(self):
        for i in self.productList:
            url = self.baseurl + i;
            print("Processing: " + i)
            ans = self.checkBjs(url)
            if ans in self.arr:
                sm = SendMail(ans, i, url, self.title)
                sm.sendemail()
                print('Mail sent! Check your mail')
            else:
                print(i + " Product out of stock")

    def checkBjs(self, url):
        options = Options()
        if config.USE_VIRTUAL_DISPLAY:
            options.add_argument('--no-sandbox')
            driver = webdriver.Chrome(chrome_options=options)
        else:
            options.page_load_strategy = 'eager'
            options.add_argument('--headless')
            driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
        driver.get(url)

        wait = WebDriverWait(driver, 10)
        shipbutton =''

        shipbutton_xpath = '//*[@id="addtocart-target"]'

        try:
            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shipbutton_xpath)))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        #driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        driver.implicitly_wait(3)
        try:
            shipbutton_element = driver.find_elements_by_xpath(shipbutton_xpath)
            for value in shipbutton_element:
                print(value.text)
                shipbutton = value.text if shipbutton_element else None

            if shipbutton == '':
                shipbutton = 'Ship Button Text not found on page'
        except:
            shipbutton = "Error loading page"

        try:
            self.title = driver.find_element_by_xpath('//*[@id="slot3"]/div[3]/div/app-pdp-name-and-item-number-organism/section/div[1]/h1').get_attribute("innerHTML")
            if self.title == '':
                self.title = "Title not found on page"

        except:
            self.title = "Page not loaded"


        print("Here is the ship button text: " + shipbutton)

        #close the browser
        driver.quit()
        return shipbutton
