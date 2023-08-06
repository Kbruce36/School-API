from django.db import models

# Create your models here.


class StaffMember(models.Model):
    first_name = models.CharField(max_length=250)
    second_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
    age = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    def __str__(self):
        return self.first_name+" "+self.second_name


class Student(models.Model):
    first_name = models.CharField(max_length=250)
    second_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name+" "+self.second_name


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    def __str__(self):
        return self.course_name

class Department(models.Model):
    department_name = models.CharField(max_length=50)
    staff = models.CharField(max_length=250)
    head_of_department = models.CharField(max_length=250)
    courses_in_department = models.CharField(max_length=250)
    def __str__(self):
        return self.department_name

class Club(models.Model):
    club_name = models.CharField(max_length=50)
    head_of_club = models.CharField(max_length=250)
    def __str__(self):
        return self.club_name