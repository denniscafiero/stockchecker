
# Python script for Amazon product availability checker
# importing libraries

from targetproducts import Target
from walmartproducts import Walmart

import time
import schedule


# times after every 1 minute
def job():
    print("Tracking....")
    #az = Amazon()
    #az.readAmazon()

    target = Target()
    target.readTarget()
    walmart = Walmart()
    walmart.readWalmart()

job()
schedule.every(15).minutes.do(job)

while True:
    # running all pending tasks/jobs
    schedule.run_pending()
    time.sleep(1)
