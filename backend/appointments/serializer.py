from rest_framework import serializers
from .models import AppointmentRescheduleRequest

class RescheduleRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentRescheduleRequest
        fields = ['appointment', 'suggested_start_time', 'suggested_end_time']