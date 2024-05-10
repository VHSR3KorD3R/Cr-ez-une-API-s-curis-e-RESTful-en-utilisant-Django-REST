from rest_framework import permissions
from api.models import Projects

class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author_id == request.user
    
class IsContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user in Projects.objects.filter(project_id=request.project_id):
            return True