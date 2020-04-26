
# Python script for Amazon product availability checker
# importing libraries

from targetproducts import Target

import time
import schedule


# times after every 1 minute
def job():
    print("Tracking....")
    #az = Amazon()
    #az.readAmazon()

    az = Target()
    az.readTarget()

job()
schedule.every(15).minutes.do(job)

while True:
    # running all pending tasks/jobs
    schedule.run_pending()
    time.sleep(1)
