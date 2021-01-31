from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, DjangoModelPermissions

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff

class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='Manager'):
            return True
        return False