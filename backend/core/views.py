from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from appointments.models import AppointmentRescheduleRequest
from appointments.serializer import RescheduleRequestViewSerializer
from .models import Company, Auditor, Audit
from .serializers import UserRegistrationSerializer, CompanyInfoSerializer, AuditorManagementSerializer, AuditSerializer


@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny])
def register_admin(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():

            user = serializer.save()
            if request.data.get('auditor_id') is not None:
                auditor = Auditor.objects.filter(pk=request.data.get('auditor_id')).first()
                auditor.user = user
                auditor.save()
            return Response({"data": "User has been created successfully"}, 201)
        else:
            return Response(serializer.errors, 400)


@api_view(['GET','POST'])
@permission_classes([AllowAny])
def companyCreation(request):
    if request.method == 'POST':
        serializer = CompanyInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Company Created Successfully'}, 201)
        else:
            return Response(serializer.errors, 400)

    else:
        items = Company.objects.all()
        serializer = CompanyInfoSerializer(instance=items, many=True)
        return Response(serializer.data, 200)

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def get_companies(request):
    companies= Company.objects.all()
    serializer=CompanyInfoSerializer(instance=companies, many=True)
    return Response(serializer.data, 200)

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def add_company(request):
    if request.method == 'POST':
        serializer=CompanyInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':'created successfully'}, 201)
        else:
            return Response(serializer.errors, 400)

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def edit_companies(request,id):
    company= Company.objects.get(pk=id)
    if request.method == 'GET':
        serializer=CompanyInfoSerializer(instance=company)
        return Response(serializer.data , status=200)
    else:
        serializer = CompanyInfoSerializer(data=request.data, instance=company)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': 'changes saved successfully'}, 201)
        else:
            return Response(serializer.errors, 400)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_company(request,id):
    comp =Company.objects.get(pk=id)
    comp.delete()
    return Response({'data':'deleted successfully'})


@api_view(['GET','POST'])
@permission_classes([AllowAny])
def get_auditors(request):
    auditor= Auditor.objects.all()
    serializer=AuditorManagementSerializer(instance=auditor, many=True)
    return Response(serializer.data, 200)


@api_view(['GET','POST'])
@permission_classes([AllowAny])
def add_Auditors(request):
    if request.method == 'POST':
        serializer=AuditorManagementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':'created successfully'}, 201)
        else:
            return Response(serializer.errors, 400)


@api_view(['GET','POST'])
@permission_classes([AllowAny])
def edit_Auditors(request,id):
    auditor = Auditor.objects.get(pk=id)
    if request.method== "GET":
        serializer=AuditorManagementSerializer(instance=auditor,many= False)
        return Response(serializer.data, 200)
    if request.method == 'POST':
        serializer=AuditorManagementSerializer(data=request.data, instance=auditor)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':'changes saved successfully'}, 200)
        else:
            return Response(serializer.errors, 400)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_auditors(request,id):
    audi=Auditor.objects.get(pk=id)
    audi.delete()
    return Response({'data':'deleted successfully'})


@api_view(['GET'])
@permission_classes([AllowAny])
def notifications(request):
    # TODO: change to requests that are only upcoming i.e. s_s_d > curr_time
    reschedule_requests = AppointmentRescheduleRequest.objects.all()
    serializer = RescheduleRequestViewSerializer(instance=reschedule_requests, many=True)
    return Response(serializer.data, 200)


@api_view(['POST'])
@permission_classes([AllowAny])
def accept_reschedule_req(request, r_id):
    reschedule_request = AppointmentRescheduleRequest.objects.filter(pk=r_id).first()
    appointment = reschedule_request.appointment
    appointment.start_time = reschedule_request.suggested_start_time
    appointment.end_time = reschedule_request.suggested_end_time
    appointment.save()
    reschedule_request.delete()
    return Response({"data": "appointment updated successfully"}, 200)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def del_notifications(request, r_id):
    reschedule_requests = AppointmentRescheduleRequest.objects.filter(pk=r_id).first()
    reschedule_requests.delete()
    return Response({"data": "deleted successfully"}, 200)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_auditHistory(request):
    audit= Audit.objects.all()
    serializer=AuditSerializer(instance=audit, many=True)
    return Response(serializer.data, 200)