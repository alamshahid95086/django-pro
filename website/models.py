from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200)
    college=models.CharField(max_length=200)
    age=models.IntegerField(max_length=10)
    is_active=models.BooleanField(default=False)
    

class Employee(models.Model):
    name=models.CharField(max_length=50)
    employee_id=models.IntegerField(max_length=20)
    occupations=models.CharField(max_length=100)
    digenations=models.CharField(max_length=200)
