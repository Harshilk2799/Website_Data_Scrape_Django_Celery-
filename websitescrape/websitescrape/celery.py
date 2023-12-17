import os
from celery.schedules import crontab
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websitescrape.settings')

app = Celery('websitescrape')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "every-10-seconds": {
        "task": "App.tasks.scrape_website",
        "schedule":crontab(minute=23, hour=22),
        "args":("https://books.toscrape.com/",)
    },
    # Add more periodic tasks as needed
}