from django.contrib import admin
from .models import Employee

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_ID','first_name','last_name','gender','dob','date_joined','salary','department_ID','manager_ID','is_activte')


