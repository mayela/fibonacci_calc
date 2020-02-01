from celery import shared_task

from .models import FibonacciNumber
import json

@shared_task
def fibonnaci_number(num):
    def fibonacci(n):
        if n < 2:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    result = fibonacci(num)
    result_obj = FibonacciNumber.objects.create(number=result)
    return json.dumps(result)
