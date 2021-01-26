from django.db import models
from Department.models import Department

# Create your models here.
PERFGRADE = (
    ('EXCELLENT', 'EXCELLENT'),
    ('GOOD', 'GOOD'),
    ('AVERAGE', 'AVERAGE'),
    ('POOR', 'POOR')
    
)
class Appraisal(models.Model):
    appraisal_ID = models.AutoField("Appraisal ID", primary_key=True)
    year = models.IntegerField("Year")
    employee_ID = models.ForeignKey("Employee.Employee", on_delete=models.CASCADE)
    perf_grade = models.CharField("Performance Grade", max_length=30, choices=PERFGRADE)

    def __str__(self):
        return self.appraisal_ID

class Manager(models.Model):
    manager_ID = models.AutoField("Manager ID", primary_key=True)
    manager_name = models.CharField("Manager", max_length=30)

    def __str__(self):
        return self.manager_ID