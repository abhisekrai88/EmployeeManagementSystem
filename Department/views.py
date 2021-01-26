from rest_framework import generics
from .models import Department
from .serializers import DepartmentSerializer

# Create your views here.

class DepartmentAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializers = [DepartmentSerializer]