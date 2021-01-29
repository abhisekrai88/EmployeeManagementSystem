from rest_framework import generics
from .models import Appraisal
from Department.models import Department
from Employee.models import Employee
from .serializers import AppraisalSerializer
from Department.serializers import DepartmentSerializer
from Employee.serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
import requests

# Create your views here.

class AppraisalViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Appraisal.objects.all()
    serializer_class = AppraisalSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
  
    