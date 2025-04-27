import os
import logging

from celery import Celery
from celery.signals import celeryd_after_setup, celeryd_init

from sheets.datawarehouse import get_wh_sqlachemy_engine

from django.conf import settings

logger = logging.getLogger(__name__)

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

app = Celery("td-inspection")
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@celeryd_after_setup.connect
def setup_connection(**kwargs):
    logger.info("Creating tunnel and DWH engine.")
    get_wh_sqlachemy_engine(settings.DWH_USERNAME, settings.DWH_PASSWORD, settings.DWH_SSH_LOCAL_BIND_HOST)


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
