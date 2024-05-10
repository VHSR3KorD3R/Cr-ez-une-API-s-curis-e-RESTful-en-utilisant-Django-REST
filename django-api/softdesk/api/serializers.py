from rest_framework import serializers
from api.models import Projects, Contributors, Issues

class ProjectDetailSerializer(serializers.ModelSerializer):
    project_author = serializers.CharField(source='author_id.username', read_only=True)
    class Meta:
        model = Projects
        fields = "__all__"

class ProjectListSerializer(serializers.ModelSerializer):
    project_author = serializers.CharField(source='author_id.username', read_only=True)
    class Meta:
        model = Projects
        fields = ["id", "name", "description", "project_type", "created_time", "project_author", "contributors"]
        
    def create(self, validated_data):
        current_user = self.context.get('request').user
        validated_data['author_id'] = current_user
        project = super().create(validated_data)
        Contributors.objects.create(
            user_id = validated_data['author_id'],
            projects_id = project
        )
        return project
        
    def validate_name(self, value):
        if Projects.objects.filter(name=value).exists():
            raise serializers.ValidationError('Project name already exists')
        return value
    
class IssueDetailSerializer(serializers.ModelSerializer):
    issue_author = serializers.CharField(source='author_id.username', read_only=True)
    class Meta:
        model = Issues
        fields = "__all__"

class IssueListSerializer(serializers.ModelSerializer):
    issue_author = serializers.CharField(source='author_id.username', read_only=True)
    project_name = serializers.CharField(source='project_id.name', read_only=True)
    class Meta:
        model = Issues
        fields = ["name", "assignment_id", "project_name", "issue_author"]
        
    def create(self, validated_data):
        current_user = self.context.get('request').user
        validated_data['author_id'] = current_user
        issue = super().create(validated_data)
        return issue
    
    def validate_name(self, value):
        if Projects.objects.filter(name=value).exists():
            raise serializers.ValidationError('Issue name already exists')
        return value
    
    def validate_project_id(self, value):
        if not Projects.objects.filter(name=value).exits():
            raise serializers.ValidationError('Project does not exist')
        return value