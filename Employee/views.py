from rest_framework import generics
from .models import Employee
from Appraisal.models import Appraisal
from Department.models import Department
from .serializers import EmployeeSerializer

# Create your views here.

class EmployeeAPIView(generics.ListCreateAPIView):
    #queryset = Employee.objects.all()
    serializers = [EmployeeSerializer]
    def get_queryset(self):
        deparment_ID = self.request.department.id
        emp_id = Employee.objects.filter(deparment_ID=deparment_ID).values('department_ID')[0]['department_ID']
        return Appraisal.objects.filter(department_ID = emp_id)
