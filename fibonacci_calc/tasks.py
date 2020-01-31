from celery import Celery

from fibonacci_numbers.models import FibonacciNumber

app = Celery('tasks', broker='//', backend="")

@app.task
def fibonnaci_number(number):
    def fibonacci(n):
        if n < 2:
            return n
        else:
            return fibRec(n-1) + fibRec(n-2)
    result = fibonacci(number)
    result = FibonacciNumber.objects.create(number=result)
    return result
