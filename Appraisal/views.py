from rest_framework import generics
from .models import Appraisal
from Department.models import Department
from Employee.models import Employee
from .serializers import AppraisalSerializer
from Department.serializers import DepartmentSerializer
from Employee.serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AppraisalAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Appraisal.objects.all()
    serializer_class = AppraisalSerializer

class DepartmentAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer