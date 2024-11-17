from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializer import RescheduleRequestSerializer

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def request_reschedule(request):
    if request.method == 'POST':
        serializer = RescheduleRequestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': 'Request has been successfully submitted.'}, 201)
        else:
            return Response(serializer.errors, 400)
# Create your views here.
