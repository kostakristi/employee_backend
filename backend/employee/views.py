from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Departments, EmployeeData, JobPosition

from .serializers import AuthTokenSerializer, DepartmentSerializer, EmployeeDataSerializer, EmployeeUpdateSerializer, JobPositionSerializer, JobPositionsUpdateSerializer, UserSerializer

from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import generics


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class LoginView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializers = self.serializer_class(
            data=request.data, context={'request': request})
        serializers.is_valid(raise_exception=True)
        user = serializers.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'user_id': user.id,
            'email': user.email,
            'name': user.name
        })

@csrf_exempt
def departmentsApi(request, id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method=='POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Department added successfully",safe=False)
        return JsonResponse("Failed to add the deparment",safe=False)
    elif request.method=='PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(id=department_data['id'])
        departments_serializer = DepartmentSerializer(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Department is updated successfully",safe=False)
        return JsonResponse("Failed to update the department")
    elif request.method=="DELETE":    
        department = Departments.objects.get(id=id)
        department.delete()
        return JsonResponse("Department is deleted",safe=False)

@csrf_exempt
def jobPositionApi(request, id=0):
    if request.method=='GET':
        jobPositions = JobPosition.objects.all()
        jobPositions_serializer = JobPositionSerializer(jobPositions, many=True)
        return JsonResponse(jobPositions_serializer.data, safe=False)
    elif request.method=='POST':
        jobPosition_data = JSONParser().parse(request)
        jobPositions_serializer = JobPositionsUpdateSerializer(data=jobPosition_data)
        if jobPositions_serializer.is_valid():
            jobPositions_serializer.save()
            return JsonResponse("Job position added successfully",safe=False)
        return JsonResponse("Failed to add the job position" + jobPositions_serializer.error,safe=False)
    elif request.method=='PUT':
        jobPosition_data = JSONParser().parse(request)
        jobPosition = JobPosition.objects.get(id=jobPosition_data['id'])
        jobPositions_serializer = JobPositionsUpdateSerializer(jobPosition, data=jobPosition_data)
        if jobPositions_serializer.is_valid():
            jobPositions_serializer.save()
            return JsonResponse("Job position is updated successfully",safe=False)
        return JsonResponse("Failed to update the job position"  + jobPositions_serializer.error,safe=False)
    elif request.method=="DELETE":    
        jobPosition = JobPosition.objects.get(id=id)
        jobPosition.delete()
        return JsonResponse("Job position is deleted",safe=False)

@csrf_exempt
def employeeApi(request, id=0):
    if request.method=='GET':
        employees = EmployeeData.objects.all()
        employees_serializer = EmployeeDataSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method=='POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeUpdateSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Employee added successfully",safe=False)
        return JsonResponse("Failed to add the employee",safe=False)
    elif request.method=='PUT':
        employee_data = JSONParser().parse(request)
        employee = EmployeeData.objects.get(id=employee_data['id'])
        employees_serializer = EmployeeUpdateSerializer(employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Employee is updated successfully",safe=False)
        return JsonResponse("Failed to update the employee",safe=False)
    elif request.method=="DELETE":    
        employee = EmployeeData.objects.get(id=id)
        employee.delete()
        return JsonResponse("Employee is deleted",safe=False)
