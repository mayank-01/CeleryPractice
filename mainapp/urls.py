from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('sendmails/', views.send_mail, name='sendmail'),
    path('schedulemail/', views.schedule_mail, name='schedulemail'),
]