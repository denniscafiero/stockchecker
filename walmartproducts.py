#!C:\Python34 python

from sendmail import SendMail

#Importing packages


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options


class Walmart:
    def __init__(self):
        self.productList = ['https://www.walmart.com/ip/Lysol-Disinfectant-Spray-Crisp-Linen-38oz-2X19oz-Cleaner/51222388',
                            'https://www.walmart.com/ip/Lysol-Disinfectant-Spray-Crisp-Linen-25oz-2X12-5oz-Cleaner/37241006',
                            'https://www.walmart.com/ip/Lysol-Disinfectant-Spray-Lemon-Breeze-19oz-Cleaner/22395165',
                            'https://www.walmart.com/ip/Lysol-Disinfectant-Spray-Spring-Waterfall-19oz-Cleaner/14711874',
                            'https://www.walmart.com/ip/Lysol-Disinfectant-Spray-Citrus-Meadows-19oz-Cleaner/11027250',
                            'https://www.walmart.com/ip/Lysol-Disinfectant-Spray-Cherry-Pomegranate-19oz-Cleaner/43256031',
                            'https://www.walmart.com/ip/Lysol-Disinfectant-Spray-Mango-Hibiscus-Brand-New-Day-19oz-Cleaner/613412757',
                            'https://www.walmart.com/ip/Lysol-Disinfectant-Spray-Jasmine-Rain-19oz-Kills-Germs-Cleaner/17236821',
                            'https://www.walmart.com/ip/Lysol-Disinfectant-Spray-3ct-Max-Cover-1x19oz-Crisp-Linen-2x19oz-Cleaner/467858461',
                            'https://www.walmart.com/ip/Lysol-Disinfectant-Spray-Berry-Basil-Brand-New-Day-19oz-Cleaner/355930006',
                            'https://www.walmart.com/ip/Lysol-Disinfectant-Spray-Mandarin-Ginger-Lily-Brand-New-Day-19oz-Cleaner/979278381',
                            'https://www.walmart.com/ip/Lysol-Disinfecting-Wipes-Ocean-Fresh-Lemon-320ct-4x80ct-Cleaner/936728961',
                            'https://www.walmart.com/ip/Lysol-Disinfecting-Wipes-Lemon-Lime-Blossom-320ct-4x80ct-Cleaner/40347108',
                            'https://www.walmart.com/ip/Lysol-Disinfecting-Wipes-Ocean-Fresh-80ct/19322742',
                            'https://www.walmart.com/ip/Lysol-Handi-Pack-Disinfecting-Wipes-80ct-Lemon-Lime-Blossom/301075719',
                            'https://www.walmart.com/ip/Lysol-Disinfecting-Wipes-Brand-New-Day-Berry-Basil-80ct-Cleaner/742123701',
                            'https://www.walmart.com/ip/Lysol-Disinfecting-Wipes-Mandarin-Gingerlily-80ct-Brand-New-Day/778493310',
                            'https://www.walmart.com/ip/Lysol-Simply-Daily-Cleaning-Disinfecting-Wipes-80ct-No-Harsh-Chemicals-Plant-based-Ingredient/448116947',
                            'https://www.walmart.com/ip/Lysol-Disinfecting-Wipes-Ocean-Fresh-80ct/19322742',
                            'https://www.walmart.com/ip/Lysol-Disinfecting-Wipes-2-Lemon-Lime-1-Mango-Hibiscus-105ct-3X35ct-Brand-New-Day/854887879',
                            'https://www.walmart.com/ip/Lysol-Kitchen-Pro-Antibacterial-Disinfecting-Wipes-30ct-Kills-Germs/146817584',
                            'https://www.walmart.com/ip/Lysol-All-Purpose-Cleaner-Spray-Lemon-Breeze-Kills-Germs-2X32oz/483952655',
                            'https://www.walmart.com/ip/Lysol-All-Purpose-Cleaner-Spray-Mandarin-Ginger-Lily-32-oz-Brand-New-Day/554300688'
                            ]
        self.baseurl = ''
        self.numberOfMinutes = 1
        self.arr = ['Add to cart']
        self.title = ""

    def readWalmart(self):
        # Asin Id is the product Id which
        # needs to be provided by the user
        # Asin = 'B0002LCZ6O'
        # get products

        # Asin = 'B07G8PW5Y3'
        # url = "http://www.amazon.com/dp/" + Asin
        for i in self.productList:
            url = self.baseurl + i;
            print("Processing: " + i)
            ans = self.checkWalmart(url)
            if ans in self.arr:
                sm = SendMail(ans, i, url, self.title)
                sm.sendemail()
                print('Mail sent! Check your mail')
            else:
                print(i + " Product out of stock")

    def checkWalmart(self, url):
        options = Options()
        options.page_load_strategy = 'eager'
        options.add_argument('--headless')

        driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
        driver.get(url)

        wait = WebDriverWait(driver, 10)
        shipbutton =''

        shipbutton_xpath = "/html/body/div[1]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div[1]/section/div[1]/div[3]/button/span/span"

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
        self.title = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[3]/div[5]/div/div[3]/div/h1').text
        for value in shipbutton_element:
            print(value.text)
            shipbutton = value.text if shipbutton_element else None

        print("Here is the ship button text: " + shipbutton)

        #close the browser
        driver.quit()
        return shipbutton
