from django.db import models
from core.models import User
from core.models import Company
class Appointment(models.Model):
    STATUS= (
        ("PENDING", "PENDING"),
        ("CONFIRM", "CONFIRM"),
        ("CANCEL","CANCEL")
    )
    assigned_by=models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_appointments")
    assigned_to=models.ForeignKey(User, on_delete=models.CASCADE, related_name="auditor_appointments")
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    start_time=models.DateTimeField(auto_now_add=False, blank=True, null=True)
    end_time=models.DateTimeField(auto_now_add=False, blank=True, null=True)
    status = models.CharField(max_length=20, default="CONFIRM")


class AppointmentRescheduleRequest(models.model):
    status = (
        ('Confirmed',"Confirmed"),
        ('Pending',"Pending"),
        ('Pending',"Pending"),
        ('Canceled',"Canceled")
    )
    appointment_id = models.ForeignKey(Appointment)
    sent_to = models.ForeignKey(User,on_delete=models.CASCADE)
    sent_by = models.ForeignKey(User)
    suggested_start_time = models.DateTimeField(auto_now_add=False)
    suggested_end_time = models.DateTimeField(auto_now_add=False)
    
    