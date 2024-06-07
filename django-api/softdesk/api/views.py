from django.shortcuts import render
from api.models import Projects, Issues, Comments
from rest_framework import viewsets, status
from rest_framework.response import Response
from api.serializers import ProjectDetailSerializer, ProjectListSerializer, IssueDetailSerializer, IssueListSerializer, ContributorSerializer, CommentDetailSerializer, CommentListSerializer
from api.models import Contributors
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsAuthor, IsContributor

# class d:
    
#     detail_serializer_class = None
    
#     def get_serializer_class(self):
#         if self.action == 'delete' and self.detail_serializer_class is not None:
#             return self.detail_serializer_class
#         return super().get_seriliazer_class()

class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated(), IsAuthor()]
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    
    def get_queryset(self):
        return Projects.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['retrieve', 'update', 'partial_update', 'create']:
            return self.detail_serializer_class
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated()]
            return [IsAuthenticated()]
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAuthenticated(), IsAuthor()]
            return [IsAuthenticated(), IsAuthor()]
        #return super(self.__class__, self).get_permissions()
        return [IsAuthenticated()]
    
    def destroy(self, request, *args, **kwargs):
        project = self.get_object()
        self.perform_destroy(project)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class IssueViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated(), IsAuthor()]
    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer
    
    def get_queryset(self):
        project_id = self.request.GET.get('project_id')
        if project_id is not None:
            queryset = Issues.objects.filter(project_id=project_id)
            return queryset
        return Issues.objects.all()
        # return Issues.objects.filter(project_id=self.kwargs["project_id"])
    
    def get_serializer_class(self):
        if self.action in ['retrieve', 'update', 'partial_update', 'create']:
            return self.detail_serializer_class
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated(), IsContributor()]
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAuthenticated(), IsAuthor()]
            return [IsAuthenticated(), IsAuthor()]
        #return super(self.__class__, self).get_permissions()
        return [IsAuthenticated()]
    
class ContributorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated(), IsAuthor()]
    serializer_class = ContributorSerializer
    
    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update', 'create']:
            self.permission_classes = [IsAuthenticated(), IsContributor()]
            return [IsAuthenticated(), IsContributor()]
        return [IsAuthenticated()]
    
class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated(), IsAuthor()]
    serializer_class = CommentListSerializer
    detail_serializer_class = CommentDetailSerializer
    
    def get_queryset(self):
        issue_id = self.request.GET.get('issue_id')
        if issue_id is not None:
            queryset = Comments.objects.filter(issue_id=issue_id)
            return queryset
        return Comments.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['retrieve', 'update', 'partial_update', 'create']:
            return self.detail_serializer_class
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated(), IsContributor()]
            return [IsAuthenticated(),IsContributor()]
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAuthenticated(), IsAuthor(), IsContributor()]
            return [IsAuthenticated(), IsAuthor(), IsContributor()]
        #return super(self.__class__, self).get_permissions()
        return [IsAuthenticated()]