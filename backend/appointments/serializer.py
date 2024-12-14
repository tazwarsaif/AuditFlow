from rest_framework import serializers

from core.serializers import CompanyInfoSerializer
from .models import Appointment, AppointmentRescheduleRequest


class AppointmentSerializer(serializers.ModelSerializer):
    company = CompanyInfoSerializer()
    assignee = serializers.SerializerMethodField()
    assigned = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ['id', "assignee", "assigned", 'assigned_by', 'assigned_to', "company", "start_time", "end_time", "status"]
        read_only_fields = ['id']

    def get_assignee(self, obj):
        return obj.assigned_by.get_full_name()

    def get_assigned(self, obj):
        return f"{obj.assigned_to.first_name} {obj.assigned_to.last_name}"


class AppointmentCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ['assigned_by', 'assigned_to', "company", "start_time", "end_time", "status"]


class RescheduleRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentRescheduleRequest
        fields = ['appointment', 'suggested_start_time', 'suggested_end_time']


class RescheduleRequestViewSerializer(serializers.ModelSerializer):
    appointment_info = serializers.SerializerMethodField()
    request_sent_by = serializers.SerializerMethodField()

    class Meta:
        model = AppointmentRescheduleRequest
        fields = ['pk', 'appointment_info', 'request_sent_by', 'suggested_start_time', 'suggested_end_time']

    def get_appointment_info(self, obj):
        return {
            "company_name": obj.appointment.company.name,
            "appointment_id": obj.appointment.pk
        }

    def get_request_sent_by(self, obj):
        return obj.sent_by.get_full_name()
