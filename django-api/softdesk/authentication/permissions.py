from rest_framework import permissions
from api.models import Projects, Issues
from django.shortcuts import get_object_or_404

class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author_id == request.user
    
class IsContributor(permissions.BasePermission):
    def has_permission(self, request, view):
        print('inside')
        print(request.user)
        #current_user = self.context.get('request').user
        project = None
        if 'projects_id' in request.data:
            queryset = Projects.objects.all()
            project = get_object_or_404(queryset, pk=request.data['projects_id'])
        if 'issue_id' in request.data:
            queryset = Issues.objects.all()
            issue = get_object_or_404(queryset, pk=request.data['issue_id'])
            project = issue.project_id
        #ajouter un autre méthode de ré
        if project is not None and request.user in project.contributors.all():
            print(request.user)
            return True
        # if request.user in Projects.objects.filter(project_id=request.project_id):
        #     return True
        return False