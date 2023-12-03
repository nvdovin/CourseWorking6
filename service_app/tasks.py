# Create your tasks here

from service_app import models as m

from celery import shared_task
from celery import Celery 
from celery.schedules import crontab
from django.core.mail import send_mail

from config.celery import app


app = Celery("config", broker='redis://localhost:6379/0')

