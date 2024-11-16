from django.urls import path

from .views import *

urlpatterns = [
    path('auth/register/', register_admin),
]
