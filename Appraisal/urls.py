from django.urls import path
from Appraisal import views

urlpatterns = [
    path(r'Appraisal', views.AppraisalAPIView.as_view(), name='Appraisal-list'),
    path(r'Employee', views.EmployeeAPIView.as_view(), name='Employee-list'),
    path(r'Department', views.DepartmentAPIView.as_view(), name='Department-list')


]