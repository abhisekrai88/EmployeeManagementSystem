from django.db import models

# Create your models here.
class Department(models.Model):
    department_ID = models.AutoField("Department ID", primary_key=True)
    department_name = models.CharField("Department Name", max_length=30)
    is_active=models.BooleanField(verbose_name='is active',default=True)

    def __str__(self):
        return (str(self.department_ID))+" - "+(self.department_name)