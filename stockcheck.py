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


# times after every 1 minute
def job():
    print("Tracking....")
    if config.COSTCO:
        costco = Costco()
        costco.readCostco()
    if config.AMAZON:
        az = Amazon()
        az.readAmazon()
    if config.TARGET:
        target = Target()
        target.readTarget()
    if config.WALMART:
        walmart = Walmart()
        walmart.readWalmart()
    if config.BJS:
        bjs = Bjs()
        bjs.readBjs()


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
