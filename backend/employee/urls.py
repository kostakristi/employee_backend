from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('signup/', views.CreateUserView.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name="login"),
    re_path(r'^department$', views.departmentsApi, name='departmentsApi'),
    re_path(r'^department/([0-9]+)$', views.departmentsApi, name='departmentsApi'),
    re_path(r'^position$', views.jobPositionApi, name='jobPositionApi'),
    re_path(r'^position/([0-9]+)$', views.jobPositionApi, name='jobPositionApi'),
    re_path(r'^employee$', views.employeeApi, name='employeeApi'),
    re_path(r'^employee/([0-9]+)$', views.employeeApi, name='employeeApi')
]

urlpatterns = format_suffix_patterns(urlpatterns)