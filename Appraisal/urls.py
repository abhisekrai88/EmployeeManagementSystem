from django.urls import path, include
from Appraisal import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Appraisal', views.AppraisalViewSet)
router.register(r'Employee', views.EmployeeViewSet)
router.register(r'Department', views.DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))


]