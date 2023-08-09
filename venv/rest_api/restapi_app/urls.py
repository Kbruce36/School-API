from django.urls import path
from . import views

# 
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from .api_info import api_info


schema_view = get_schema_view(
    info=api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('staff/', views.staff_list),
    path('staff/<int:pk>', views.staff_detail), 
    path('students/', views.student_list),
    path('students/<int:pk>', views.student_detail),
    path('departments/', views.department_list),
    path('departments/<int:pk>', views.department_detail),
    path('clubs/', views.club_list),
    path('clubs/<int:pk>', views.club_detail),
    path('courses/', views.course_list),
    path('courses/<int:pk>', views.course_detail),
    # Modifying with swagger file
    path('', views.index, name="index"),
]


# 
# Include the Swagger and ReDoc URLs
urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
