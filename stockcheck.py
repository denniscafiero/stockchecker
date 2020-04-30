# Python script for Amazon product availability checker
# importing libraries

from targetproducts import Target
from walmartproducts import Walmart
from bjsproducts import Bjs
from costcoproducts import Costco
from amazonproducts import Amazon
from pyvirtualdisplay import Display

import time
import schedule
import config
import threading


# times after every 1 minute
def job():

    thread_list = list()
    print("Tracking....")
    if config.COSTCO:
        costco = Costco()
        costco.readCostco()
    if config.AMAZON:
        az = Amazon()
        az.readAmazon()
    if config.TARGET:
        target = Target()
        t = threading.Thread(name='Target Thread {}'.format(0), target=target.readTarget)
        t.start()
        time.sleep(1)
        print(t.name + ' started')
        thread_list.append(t)

    if config.WALMART:
        walmart = Walmart()
        t = threading.Thread(name='Walmart Thread {}'.format(1), target=walmart.readWalmart)
        t.start()
        time.sleep(1)
        print(t.name + ' started')
        thread_list.append(t)
    if config.BJS:
        bjs = Bjs()
        t = threading.Thread(name='BJs Thread {}'.format(2), target=bjs.readBjs)
        t.start()
        time.sleep(1)
        print(t.name + ' started')
        thread_list.append(t)

    #Wait for all threads to complete
    for thread in thread_list:
        thread.join()

    print('Thread and scraping complete')


if config.USE_VIRTUAL_DISPLAY:
    display = Display(visible=0, size=(800, 600))
    display.start()
    print("virtual display run")

job()

schedule.every(config.DELAY_IN_MINUTES).minutes.do(job)

while True:
    # running all pending tasks/jobs
    schedule.run_pending()
    time.sleep(1)
