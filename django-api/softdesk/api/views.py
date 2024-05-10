from django.shortcuts import render
from api.models import Projects, Issues
from rest_framework import viewsets
from api.serializers import ProjectDetailSerializer, ProjectListSerializer, IssueDetailSerializer, IssueListSerializer
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsAuthor, IsContributor

# class d:
    
#     detail_serializer_class = None
    
#     def get_serializer_class(self):
#         if self.action == 'delete' and self.detail_serializer_class is not None:
#             return self.detail_serializer_class
#         return super().get_seriliazer_class()

class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated(), IsAuthor]
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    
    def get_queryset(self):
        return Projects.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['retrieve', 'update', 'partial_update']:
            return self.detail_serializer_class
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAuthenticated(), IsAuthor]
            return [IsAuthenticated(), IsAuthor]
        #return super(self.__class__, self).get_permissions()
        return [IsAuthenticated()]
    
class IssueViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated(), IsAuthor]
    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer
    
    def get_queryset(self):
        return Issues.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['retrieve', 'update', 'partial_update']:
            return self.detail_serializer_class
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated(), IsContributor()]
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAuthenticated(), IsAuthor]
            return [IsAuthenticated(), IsAuthor]
        #return super(self.__class__, self).get_permissions()
        return [IsAuthenticated()]