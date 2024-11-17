from django.urls import path,include

from .views import *

urlpatterns = [
    path('auth/register/', register_admin),
    path('company/add/',companyCreation)
]
