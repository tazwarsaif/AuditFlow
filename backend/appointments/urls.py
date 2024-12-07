from django.urls import path
from .views import *

urlpatterns = [
    path('request-reschedule/', request_reschedule),

    path('appointments/', get_appointments),
    path('add-appointment/', add_appointment),
    path('del-appointment/<str:id>', delete_appointment),
]