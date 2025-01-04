from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.models import Auditor
from .models import Appointment
from .serializer import RescheduleRequestSerializer, AppointmentSerializer, AppointmentCreationSerializer


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def request_reschedule(request):
    if request.method == 'POST':
        app = Appointment.objects.filter(pk=request.data['appointment']).first()
        admin = app.assigned_by
        serializer = RescheduleRequestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.validated_data['sent_to'] = admin
            serializer.validated_data['sent_by'] = request.user
            serializer.save()
            return Response({'data': 'Request has been successfully submitted.'}, 201)
        else:
            return Response(serializer.errors, 400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_appointments(request):
    user = request.user
    print(user.user_type)
    if user.user_type == 'ADMIN':
        appointments = Appointment.objects.all().order_by('start_time')
    else:
        auditor = user.auditor
        appointments = Appointment.objects.filter(assigned_to=auditor).order_by('start_time')
    serializer = AppointmentSerializer(instance=appointments, many=True)
    return Response(serializer.data, 200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_appointment(request):
    if request.method == 'POST':
        data = request.data.copy()
        data['assigned_by'] = request.user.pk
        serializer = AppointmentCreationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 201)
        else:
            return Response(serializer.errors, 400)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_appointment(request, id):
    appointment = Appointment.objects.filter(pk=id).first()
    appointment.delete()
    return Response({'data': 'appointment has been deleted'}, 200)
