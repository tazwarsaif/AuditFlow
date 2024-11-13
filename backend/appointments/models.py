from django.db import models
from core.models import User

class AppoinmentRescheduleRequest(models.model):
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
    
    