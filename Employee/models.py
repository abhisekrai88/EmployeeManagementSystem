from djmoney.models.fields import MoneyField
from django.db import models
from Department.models import Department

# Create your models here.

class Employee(models.Model):
    employee_ID = models.AutoField("Employee ID", primary_key=True)
    first_name = models.CharField("First Name", max_length=30)
    last_name = models.CharField("Last Name", max_length=30)
    gender = models.CharField("Gender(M/F)", max_length=1)
    dob = models.DateField("Date of Birth")
    date_joined = models.DateField("Date Joined")
    salary = models.MoneyField("Salary", max_digits=10, decimel_places=2, default_currency='SGD')
    department_ID = models.ForeignKey(Department, on_delete=models.CASCADE)
