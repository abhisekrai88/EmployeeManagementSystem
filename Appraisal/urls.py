from django.urls import path, include
from Appraisal import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Appraisal', views.AppraisalViewSet, 'Appraisal')
router.register(r'Employee', views.EmployeeViewSet, 'Employee')
router.register(r'Department', views.DepartmentViewSet, 'Department')
router.register(r'ManagerViewSet',views.ManagerViewSet,'Manager')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))


]