from django.urls import path
from . import views

urlpatterns = [
    path('staff/', views.staff_list),
    path('staff/<int:pk>', views.staff_detail),
    path('students/', views.student_list),
    path('students/<int:pk>', views.student_detail),
    path('departments/', views.department_list),
    path('departments/<int:pk>', views.department_detail),
    path('clubs/', views.club_list),
    path('clubs/<int:pk>', views.club_detail),
]
