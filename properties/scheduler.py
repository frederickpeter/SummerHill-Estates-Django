from apscheduler.schedulers.background import BackgroundScheduler
from .views import incomplete_reservations

# to import the ghana timezone
from django.conf import settings

# Create scheduler to run in a thread inside the application process
scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)

def start():
    # print("peter")

    # Adding this job here instead.
    # everyday  or rather every 24 hours
    # scheduler.add_job(incomplete_reservations, 'interval', days=1, start_date='2020-08-23 08:45:00', id="incomplete_reservations",replace_existing=True)
    
    #every 6 hours
    scheduler.add_job(incomplete_reservations, 'interval', hours=6, start_date='2020-08-23 00:00:00', id="incomplete_reservations2",replace_existing=True)


    scheduler.start()