from rest_framework import serializers

from .models import FibonacciNumber
    
class FibonacciNumberSerializer(serializers.Serializer):
    number = serializers.IntegerField(read_only=True)