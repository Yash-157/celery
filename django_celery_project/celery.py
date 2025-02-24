from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')
app= Celery('django_celery_project')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')

# celery beat settings 

app.conf.beat_schedule = {
    'send-mail-every-day':{
        'task' : 'send_mail_app.tasks.send_mail_func',
        'schedule' : crontab(minute=12, hour=11),

    }
}

app.autodiscover_tasks()

app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')