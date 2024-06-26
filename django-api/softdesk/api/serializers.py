from rest_framework import serializers
from api.models import Projects, Contributors, Issues, Comments

class ProjectDetailSerializer(serializers.ModelSerializer):
    project_author = serializers.CharField(source='author_id.username', read_only=True)
    class Meta:
        model = Projects
        fields = ["project_author", "name", "description", "project_type", "created_time", "contributors"]
    
    def create(self, validated_data):
        current_user = self.context.get('request').user
        validated_data['author_id'] = current_user
        project = super().create(validated_data)
        Contributors.objects.create(
            user_id = validated_data['author_id'],
            projects_id = project
        )
        return project
    
    def partial_update(self, validated_data):
        print("test")
        project = self.get_object()
        print("test")
        Contributors.objects.create(
            user_id = validated_data['contributors'],
            projects_id = project
        )
        project.contributors = validated_data['contributors']
        serializer = ProjectDetailSerializer(project, partial=True)
        return serializer
        

class ProjectListSerializer(serializers.ModelSerializer):
    project_author = serializers.CharField(source='author_id.username', read_only=True)
    class Meta:
        model = Projects
        fields = ["name", "description", "project_type", "created_time", "project_author"]
        
    def validate_name(self, value):
        if Projects.objects.filter(name=value).exists():
            raise serializers.ValidationError('Project name already exists')
        return value

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = "__all__"
    
    def create(self, validated_data):
        user_projects = Contributors.objects.filter(user_id=validated_data["user_id"], projects_id=validated_data['projects_id'])
        contributor = None
        if not user_projects:
            contributor = Contributors.objects.create(
                user_id = validated_data['user_id'],
                projects_id = validated_data['projects_id']
            )
        return contributor
    
class IssueDetailSerializer(serializers.ModelSerializer):
    issue_author_name = serializers.CharField(source='author_id.username', read_only=True)
    project_name = serializers.CharField(source='project_id.name', read_only=True)
    class Meta:
        model = Issues
        fields = ["project_name", "issue_author_name", "name", "description", "priority", "issue_type", "progress", "assignment_id", "project_id"]
    
    def create(self, validated_data):
        current_user = self.context.get('request').user
        validated_data['author_id'] = current_user
        issue = super().create(validated_data)
        return issue

class IssueListSerializer(serializers.ModelSerializer):
    issue_author_name = serializers.CharField(source='author_id.username', read_only=True)
    project_name = serializers.CharField(source='project_id.name', read_only=True)
    class Meta:
        model = Issues
        fields = ["project_name", "name", "priority", "issue_type", "progress", "assignment_id", "issue_author_name"]
    
    def validate_name(self, value):
        if Projects.objects.filter(name=value).exists():
            raise serializers.ValidationError('Issue name already exists')
        return value
    
    def validate_project_id(self, value):
        if not Projects.objects.filter(name=value).exits():
            raise serializers.ValidationError('Project does not exist')
        return value
    
class CommentDetailSerializer(serializers.ModelSerializer):
    comment_author_name = serializers.CharField(source='author_id.username', read_only=True)
    class Meta:
        model = Comments
        fields = ["comment_author_name", "description", "issue_id", "created_time"]
    
    def create(self, validated_data):
        print("create comment")
        print(validated_data)
        current_user = self.context.get('request').user
        validated_data['author_id'] = current_user
        comment = super().create(validated_data)
        return comment

class CommentListSerializer(serializers.ModelSerializer):
    comment_author_name = serializers.CharField(source='author_id.username', read_only=True)
    class Meta:
        model = Comments
        fields = ["issue_id", "comment_author_name", "description"]
    
    def validate_issue_id(self, value):
        if not Issues.objects.filter(name=value).exits():
            raise serializers.ValidationError('Issue does not exist')
        return value