from django.urls import path
from .views import *

urlpatterns = [
    path('request-reschedule/', request_reschedule)
]