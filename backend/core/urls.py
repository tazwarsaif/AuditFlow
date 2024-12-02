from django.urls import path,include

from .views import *

urlpatterns = [
    path('auth/register/', register_admin),
    path('company/add/',companyCreation),
    path('auditors/', get_auditors),
    path('auditors/add/', add_Auditors),
    path('auditors/edit/<str:id>', edit_Auditors),
    path('auditors/delete/<str:id>', delete_auditors)
]
