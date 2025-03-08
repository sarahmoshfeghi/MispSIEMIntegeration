import schedule
import time
#from mailsend import send_mail
from MispToQradarRefrence import run_ioc_process
def job():
    print("Running scheduled task...")
    run_ioc_process()
    #send_mail("test@gmail.com")

# Schedule the job every day at 11:00 AM
#schedule.every(12).hours.do(job)
#schedule.every().day.at("11:00").do(job)

# Schedule the job every day at 4:00 PM (16:00)
schedule.every().day.at("09:57").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
