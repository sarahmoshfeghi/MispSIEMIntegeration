import schedule
import time

from update_qradar_refrenceset import run_ioc_process
def job():
    print("Running scheduled task...")
    run_ioc_process()
#schedule.every(12).hours.do(job)
#schedule.every().day.at("11:00").do(job)

# Schedule the job every day at 9:00 AM 
schedule.every().day.at("09:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
