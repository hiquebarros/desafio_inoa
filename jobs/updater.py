from apscheduler.schedulers.background import BackgroundScheduler
from jobs.jobs import schedule_update

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(schedule_update, 'interval', seconds=5)
	scheduler.start()