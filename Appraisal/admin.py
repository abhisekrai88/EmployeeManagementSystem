from django.contrib import admin
from .models import Appraisal, Manager


# Register your models here.

@admin.register(Appraisal)
class AppraisalAdmin(admin.ModelAdmin):
    list_display = ('appraisal_ID', 'employee_ID', 'perf_grade','year')

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('manager_ID', 'manager_name')




