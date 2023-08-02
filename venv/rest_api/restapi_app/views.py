from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

#Staff views
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

# Student views
@api_view(['POST','GET'])
def student_list(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
    elif request.method == 'GET':
        staff = Student.objects.all()
        serializer = StudentSerializer(staff, many=True)
    return Response(serializer.data)

@api_view(['GET', 'UPDATE', 'DELETE'])
def student_detail(request,pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    elif request.method == 'UPDATE':
        serializer = StudentSerializer(student, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Departments Views

@api_view(['POST','GET'])
def department_list(request):
    if request.method == 'POST':
        serializer = DepartmentSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        department = Department.objects.all()
        serializer = StaffSerializer(department, many=True)
        return Response(serializer.data)



@api_view(['GET', 'PUT', 'DELETE'])
def department_detail(request,pk):
    department = Department.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DepartmentSerializer(department, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Clubs Views

@api_view(['POST','GET'])
def club_list(request):
    if request.method == 'POST':
        serializer = ClubSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        club = Club.objects.all()
        serializer = ClubSerializer(club, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def club_detail(request,pk):
    club = Club.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = ClubSerializer(club)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ClubSerializer(club, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        club.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)