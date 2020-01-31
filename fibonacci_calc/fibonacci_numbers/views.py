from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import FibonacciNumber
from .serializers import FibonacciNumberSerializer

@api_view(['GET'])
def get_fibonacci_numbers_list(request):
    fibonacci_numbers = FibonacciNumber.objects.all()
    serializer = FibonacciNumberSerializer(fibonacci_numbers, many=True)
    return Response(serializer.data)

