from django.contrib import admin
from .models import Appraisal, Manager
from Department.models import Department
from Employee.models import Employee

# Register your models here.

@admin.register(Appraisal)
class AppraisalAdmin(admin.ModelAdmin):
    list_display = ('appraisal_ID', 'employee_ID', 'perf_grade','year')

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('manager_ID', 'manager_name')

##@admin.register(Employee)
#class EmployeeAdmin(admin.ModelAdmin):
    #search_fields = ('first_name', 'last_name')

   # list_display = ('first_name', 'last_name', 'department_name', 'perf_grade', 'year')

