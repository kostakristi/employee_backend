from django.db import models

# Create your models here.
class Departments(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class JobPosition(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class EmployeeData(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    salary = models.FloatField()
    hire_date = models.DateField()
    job_position = models.ForeignKey(JobPosition, on_delete=models.CASCADE)

    def __str__(self):
        return self.name