from django.contrib import admin

from .models import Appointment, AppointmentRescheduleRequest

# Register your models here.
admin.site.register([Appointment, AppointmentRescheduleRequest])