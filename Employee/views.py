from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.

class EmployeeAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializers = [EmployeeSerializer]
