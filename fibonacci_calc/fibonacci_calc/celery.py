import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fibonacci_calc.settings')

app = Celery('fibonacci_calc')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()