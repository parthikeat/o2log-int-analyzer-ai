import schedule
import time
from ai_log_analyzer.main import process_logs

def job():
    print("Running log analysis...")
    process_logs()

schedule.every(15).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
