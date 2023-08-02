from django.urls import path
from . import views

urlpatterns = [
    path('staff/', views.staff_list),
    path('staff/<int:pk>', views.staff_detail),
    path('student/', views.student_list),
    path('student/<int:pk>', views.student_detail),
]
