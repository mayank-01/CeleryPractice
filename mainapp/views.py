from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from sendmail.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail(request):
    send_mail_func.delay()
    return HttpResponse("Sent")


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=18, minute=6)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task "+"2",task='sendmail.tasks.send_mail_func') #, args=json.dumps((2,3)))
    return HttpResponse("Done")
