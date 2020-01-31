from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import get_fibonacci_numbers_list

urlpatterns = [path('fibonacci/', get_fibonacci_numbers_list)]

urlpatterns = format_suffix_patterns(urlpatterns)