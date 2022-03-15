from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from pytz import timezone
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerytut.settings')

app = Celery('celerytut')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'send-mail-everyday-at-8':{
        'task': 'sendmail.tasks.send_mail_func',
        'schedule': crontab(hour=17, minute=46),

    }
}


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
9