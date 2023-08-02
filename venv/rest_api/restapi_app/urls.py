from django.urls import path
from . import views

urlpatterns = [
    path('staff/', views.staff_list),
    path('staff/<int:pk>', views.staff_detail),
# 
    path('course/', views.course_list),
    path('course/<int:pk>', views.course_detail),
]
