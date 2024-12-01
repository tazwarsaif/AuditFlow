from django.urls import path,include

from .views import *

urlpatterns = [
    path('auth/register/', register_admin),
    path('company/add/',companyCreation),
    path('auditors/', get_auditors),
    path('auditors/add/', add_Auditors),
    path('auditors/edit/', get_auditors),
    path('auditors/delete/', get_auditors)
]
