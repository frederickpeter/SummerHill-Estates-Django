from django.apps import AppConfig
from django.conf import settings


class PropertiesConfig(AppConfig):
    name = 'properties'

    # def ready(self):
    #     from . import scheduler
    #     if settings.SCHEDULER_AUTOSTART:
    #     	scheduler.start()
