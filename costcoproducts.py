

from sendmail import SendMail
import config

#Importing packages


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options


class Costco:
    def __init__(self):
        self.productList = ['https://www.costco.com/kirkland-signature-disinfecting-wipes,-variety-pack,-304-count.product.100413817.html',
                            'https://www.costco.com/clorox-clean-up-all-purpose-cleaner-with-bleach%2c-original%2c-32-oz-%2526-180-oz-refill.product.100146130.html',
                            'https://www.costco.com/kirkland-signature-bath-tissue,-2-ply,-425-sheets,-30-rolls.product.100142093.html',
                            'https://www.costco.com/kirkland-signature-create-a-size-paper-towels%2c-2-ply%2c-160-sheets%2c-12-count.product.100234271.html',
                            'https://www.costco.com/bounty-prints-select-a-size-paper-towels%2c-12-roll.product.100523582.html',
                            'https://www.costco.com/starbucks-french-roast%2c-whole-bean-coffee%2c-2.5-lbs.product.100377146.html'
                            ]
        self.baseurl = ''
        self.numberOfMinutes = 1
        self.arr = ['add-to-cart']
        self.title = ""

    def readCostco(self):
        for i in self.productList:
            url = self.baseurl + i;
            print("Processing: " + i)
            ans = self.checkCostco(url)
            if ans in self.arr:
                sm = SendMail(ans, i, url, self.title)
                sm.sendemail()
                print('Mail sent! Check your mail')
            else:
                print(i + " Product out of stock")

    def checkCostco(self, url):
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

        shipbutton_xpath = '//*[@id="add-to-cart-btn"]'

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
        self.title = driver.find_element_by_xpath('/html/body/div[8]/div[3]/div[3]/div[1]/div[3]/div[1]/div/div[2]/h1').get_attribute("innerHTML")
        for value in shipbutton_element:
            print(value.get_attribute("class"))
            shipbutton = value.get_attribute("class") if shipbutton_element else None

        print("Here is the ship button text: " + shipbutton)

        #close the browser
        driver.quit()
        return shipbutton
