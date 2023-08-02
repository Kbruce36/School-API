from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['POST','GET'])
def staff_list(request):
    if request.method == 'POST':
        serializer = StaffSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
    elif request.method == 'GET':
        staff = StaffMember.objects.all()
        serializer = StaffSerializer(staff, many=True)
    return Response(serializer.data)



@api_view(['GET', 'PUT', 'DELETE'])
def staff_detail(request,pk):
    staff = StaffMember.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = StaffSerializer(staff)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StaffSerializer(staff, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
