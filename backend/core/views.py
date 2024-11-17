from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Company
from .serializers import UserRegistrationSerializer, CompanyInfoSerializer



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


class Item:
    pass


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