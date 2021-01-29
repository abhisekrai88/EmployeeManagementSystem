from django.contrib import admin
from .models import Employee
from Appraisal.models import Appraisal, Manager
from Department.models import Department

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_ID','first_name','last_name','gender','dob','date_joined','salary','department_ID','manager_ID','is_active')


