import datetime
from celery.schedules import crontab
from django.utils import timezone
from celery import shared_task
from endpoints.models import Users
from datetime import datetime, timedelta


@shared_task(run_every=crontab(seconds=5))
def deleteAccount():
    pass
  
  
