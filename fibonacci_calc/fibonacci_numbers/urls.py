from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import get_fibonacci_numbers_list, calculate_fibonacci_number

urlpatterns = [
    path('fibonacci/', get_fibonacci_numbers_list),
    path('fibonacci/<int:number>', calculate_fibonacci_number)
    ]

urlpatterns = format_suffix_patterns(urlpatterns)