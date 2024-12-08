from django.db import models
from core.models import User, Auditor
from core.models import Company
class Appointment(models.Model):
    STATUS= (
        ("PENDING", "PENDING"),
        ("CONFIRM", "CONFIRM"),
        ("CANCEL","CANCEL")
    )
    assigned_by=models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_appointments")
    assigned_to=models.ForeignKey(Auditor, on_delete=models.CASCADE, related_name="auditor_appointments")
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    start_time=models.DateTimeField(auto_now_add=False, blank=True, null=True)
    end_time=models.DateTimeField(auto_now_add=False, blank=True, null=True)
    status = models.CharField(max_length=20, default="CONFIRM")

    def __str__(self):
        return f"{self.company.name}: {self.start_time.date()} to {self.end_time.date()}"


class AppointmentRescheduleRequest(models.Model):
    status = (
        ('Confirmed',"Confirmed"),
        ('Pending',"Pending"),
        ('Pending',"Pending"),
        ('Canceled',"Canceled")
    )
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    sent_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="app_requested7")
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments")
    suggested_start_time = models.DateTimeField(auto_now_add=False)
    suggested_end_time = models.DateTimeField(auto_now_add=False)
    
    