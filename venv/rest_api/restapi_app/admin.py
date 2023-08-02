from django.contrib import admin
from .models import StaffMember,Student,Course,Department,Club

# Register your models here.

admin.site.register(StaffMember)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Club)
