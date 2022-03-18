from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

from .models import Departments, EmployeeData, JobPosition


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validate_data):
        return get_user_model().objects.create_user(**validate_data)


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            email=email,
            password=password
        )
        if not user:
            raise serializers.ValidationError("Invalid Credentials")
        attrs['user'] = user
        return attrs

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('id', 'name')

class JobPositionSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    class Meta:
        model=JobPosition
        fields=('id', 'name', 'department')

class JobPositionsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields =['id','name','department']
        
class EmployeeDataSerializer(serializers.ModelSerializer):
    job_position = JobPositionSerializer(read_only=True)
    class Meta:
        model=EmployeeData
        fields=('id', 'name', 'email', 'phone', 'salary', 'hire_date', 'job_position')

class EmployeeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeData
        fields =('id', 'name', 'email', 'phone', 'salary', 'hire_date', 'job_position')