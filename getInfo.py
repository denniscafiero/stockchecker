from time import sleep

from lxml import html

import requests


class GetPageInfo():
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;     x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"
            }
        self.proxies = { # define the proxies which you want to use
            'http': '157.55.190.252:8080',
            'https': '157.55.190.252:8080',
        }

    def getUrlInfo(self):
        # adding headers to show that you are
        # a browser who is sending GET request
        page = requests.get(self.url, headers=self.headers, proxies=self.proxies)
        for i in range(20):
            # because continuous checks in
            # milliseconds or few seconds
            # blocks your request
            sleep(3)

            # parsing the html content
            doc = html.fromstring(page.content)

            return doc


