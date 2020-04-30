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


class Target:
    def __init__(self):
        self.productList = ['https://www.target.com/p/clorox-scentiva-wipes-bleach-free-cleaning-wipes-tuscan-lavender-38-jasmine-70ct/-/A-53398642',
                            'https://www.target.com/p/lysol-disinfecting-wipes-lemon-lime-blossom-80-wipes/-/A-14214467',
                            'https://www.target.com/p/lysol-disinfecting-wipes-brand-new-day-80-wipes/-/A-52404002',
                            'https://www.target.com/p/disinfecting-wipes-lemon-scent-35-ct-up-up-8482/-/A-14694518',
                            'https://www.target.com/p/clorox-citrus-blend-disinfecting-wipes-crisp-lemon/-/A-79389928',
                            'https://www.target.com/p/lysol-disinfectant-crisp-linen-spray-19-oz/-/A-14214405',
                            ]
        self.baseurl = ''
        self.numberOfMinutes = 1
        self.arr = ['Ship it']
        self.title = ""

    def readTarget(self):
        for i in self.productList:
            url = self.baseurl + i;
            print("Processing: " + i)
            ans = self.checkTarget(url)
            if ans in self.arr:
                sm = SendMail(ans, i, url, self.title)
                sm.sendemail()
                print('Mail sent! Check your mail')
            else:
                print(i + " Product out of stock")

    def checkTarget(self, url):
        options = Options()
        if config.USE_VIRTUAL_DISPLAY:
            options.add_argument('--no-sandbox')
            driver = webdriver.Chrome(chrome_options=options)
        else:
            options.page_load_strategy = 'eager'
            if config.HEADLESS_MODE:
                options.add_argument('--headless')
            driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
        driver.get(url)

        wait = WebDriverWait(driver, 10)
        shipbutton =''

        shipbutton_xpath = "//*[@id='viewport']/div[4]/div/div[2]/div[3]/div[1]/div/div/div/div[2]/div[1]/div/div[2]/div/button"

        try:
            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shipbutton_xpath)))
            print
            "Page is ready!"
        except TimeoutException:
            print
            "Loading took too much time!"
        #driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        driver.implicitly_wait(3)
        shipbutton_element = driver.find_elements_by_xpath(shipbutton_xpath)
        self.title = driver.find_element_by_xpath('//*[@id="viewport"]/div[4]/div/div[1]/div[2]/h1/span').text
        for value in shipbutton_element:
            print(value.text)
            shipbutton = value.text if shipbutton_element else None
        #shipbutton = shipbutton_element[0].text if shipbutton_element else None

        print("Here is the ship button text: " + shipbutton)

        #close the browser
        driver.quit()
        return shipbutton
