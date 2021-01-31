from Appraisal.permission import ReadOnly
from .models import Appraisal, Manager 
from Department.models import Department
from Employee.models import Employee
from .serializers import AppraisalSerializer, ManagerSerializer
from Department.serializers import DepartmentSerializer
from Employee.serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .permission import  IsManager
from rest_framework import viewsets




# Create your views here.

class AppraisalViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, ReadOnly, )
    #queryset = Appraisal.objects.all()
    serializer_class = AppraisalSerializer
    def get_queryset(self):
        user_id = self.request.user.id
        emp_id = Employee.objects.filter(user_id=user_id).values('employee_ID')[0]['employee_ID']
        return Appraisal.objects.filter(employee_ID = emp_id)
    


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsAuthenticated)

class EmployeeViewSet(viewsets.ModelViewSet):
    #queryset = Employee.objects.filter(date_of_leaving__gte=date.today())
    # queryset = Employee.objects.all()
    def get_queryset(self):
        user_id = self.request.user.id
        if self.request.user.is_superuser:
            return Employee.objects.all()
        else:
            return Employee.objects.filter(user_id=user_id)
    serializer_class = EmployeeSerializer
    permission_classes = (ReadOnly,)
    # permission_classes = (permissions.IsAdminUser,)
    
class ManagerViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        user_id = self.request.user.id
        if self.request.user.is_superuser:
             return ManagerSerializer
        else:
            return EmployeeSerializer
    def get_queryset(self):
        user_id = self.request.user.id
        if self.request.user.is_superuser:
            return Manager.objects.all()
        else:
            employee = Employee.objects.get(user_id = user_id)
            employee_id = employee.employee_ID     
            if Manager.objects.filter(employee_ID = employee_id):
                manager_id = Manager.objects.filter(employee_ID = employee_id).values('manager_ID')[0]['manager_ID']
                return Employee.objects.filter(manager_ID = manager_id)           
    permission_classes = (ReadOnly,)