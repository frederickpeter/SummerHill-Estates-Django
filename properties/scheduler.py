from apscheduler.schedulers.background import BackgroundScheduler
from .views import incomplete_reservations

from django.conf import settings

# Create scheduler to run in a thread inside the application process
scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)

def start():

    # Adding this job here instead.
    scheduler.add_job(incomplete_reservations, 'interval', days=1, start_date='2020-08-23 05:01:00', id="incomplete_reservations",replace_existing=True)
    scheduler.add_job(incomplete_reservations, 'interval', hours=12, start_date='2020-08-23 00:00:00', id="incomplete_reservations2",replace_existing=True)


    scheduler.start()