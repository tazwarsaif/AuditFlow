from django.urls import path,include

from .views import *

urlpatterns = [
    path('auth/register/', register_admin),
    path('company/add/',companyCreation),
    path('company/',get_companies),
    path('company/edit/<str:id>',edit_companies),
    path('company/delete/<str:id>',delete_company),
    path('company/add/',add_company),
    path('auditors/', get_auditors),
    path('auditors/add/', add_Auditors),
    path('auditors/edit/<str:id>', edit_Auditors),
    path('auditors/delete/<str:id>', delete_auditors),

    path('notifications/', notifications),
    path('reschedule/<str:r_id>/', accept_reschedule_req),
    path('notifications/delete/<str:r_id>/', del_notifications)
]
