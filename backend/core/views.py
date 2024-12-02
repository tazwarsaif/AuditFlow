from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Company, Auditor
from .serializers import UserRegistrationSerializer, CompanyInfoSerializer, AuditorManagementSerializer


@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny])
def register_admin(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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
