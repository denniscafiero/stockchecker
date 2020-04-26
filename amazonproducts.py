from sendmail import SendMail

from getInfo import GetPageInfo

class Amazon:
    def __init__(self):
        self.productList = ['B001E6F31K', 'B00J5HLMGA', 'B0002LCZ6O', 'B00K3U1B64', 'B00IE68EE6', 'B006RGHKPE', 'B007LKG5V0',
                            'B01DCG0GPC', 'B00MJPVQEI', 'B00LOS73DE', 'B001B150PW', 'B006TWSSQG', 'B078XXPC1Z', 'B004Y0VGH8', 'B00Q70RCW6',
                            'B07CVQ4271', 'B00GRUK048', 'B01MU7YK6R']
        self.baseurl = 'http://www.amazon.com/dp/'
        self.numberOfMinutes = 1
        self.arr = ['Only 1 left in stock.',
                    'Only 2 left in stock.',
                    'Usually ships within 3 to 5 days.',
                    'In stock.', 'In Stock.']
        self.title = ""

    def readAmazon(self):
        # Asin Id is the product Id which
        # needs to be provided by the user
        # Asin = 'B0002LCZ6O'
        # get products

        # Asin = 'B07G8PW5Y3'
        # url = "http://www.amazon.com/dp/" + Asin
        for i in self.productList:
            url = self.baseurl + i;
            print("Processing: " + i)
            ans = self.checkAmazon(url)
            if ans in self.arr:
                sm = SendMail(ans, i, url, self.title)
                sm.sendemail()
                print('Mail sent! Check your mail')
            else:
                print(i + " Product out of stock")

    def checkAmazon(self, url):
        # create the amazon class
        amazon = GetPageInfo(url);
        # call get the url content in document
        doc = amazon.getUrlInfo()


        # check the availaility
        XPATH_AVAILABILITY = '//div[@id ="availability"]//text()'
        RAw_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)
        AVAILABILITY = ''.join(RAw_AVAILABILITY).strip() if RAw_AVAILABILITY else None

        title_xpath = '//*[@id="productTitle"]//text()'

        TITLE = doc.xpath(title_xpath)
        self.title = TITLE if TITLE else None
        return AVAILABILITY
