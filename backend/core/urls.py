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
    path("audithistory/",get_auditHistory),
    path('audit-details/<str:a_id>', audit_details),
    path('audit-report/<str:a_id>', submit_report),
    path('initial-audit/<str:appointment_id>', initiate_audit),
    path('notifications/', notifications),
    path('reschedule/<str:r_id>/', accept_reschedule_req),
    path('notifications/delete/<str:r_id>/', del_notifications),

    path('get-auditor-profile/', edit_auditor_profile),
    path('leave-application/', submit_leave_application)
]
