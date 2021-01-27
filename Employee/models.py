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
    salary = MoneyField("Salary", max_digits=14, decimal_places=2  ,default_currency='SGD')
    department_ID = models.ForeignKey(Department, on_delete=models.CASCADE)
    manager_ID = models.ForeignKey("Appraisal.Manager", on_delete=models.CASCADE)
    is_active=models.BooleanField(verbose_name='is active',default=True)
    
    def __str__(self):
        return (str(self.employee_ID))+'  -  '+(self.first_name+' '+self.last_name)