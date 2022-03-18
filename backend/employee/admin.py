from django.contrib import admin

from .models import Departments, EmployeeData, JobPosition

# Register your models here.
admin.site.register(Departments)
admin.site.register(JobPosition)
admin.site.register(EmployeeData)