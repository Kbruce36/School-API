from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['POST'])
def create_staff(request):
    serializer = StaffSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)