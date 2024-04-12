from django.db import models
from datetime import date

# Create your models here.
class Projects(models.Model):
    class ProjectType(models.TextChoices):
        BACK_END = 'back-end'
        FRONT_END = 'front-end'
        IOS = 'iOS'
        ANDROID = 'Android'
        
    author_id = models.ForeignKey("authentication.User", on_delete=models.CASCADE, related_name='project_author')
    name = models.CharField(max_length=50)
    description = models.TextField(default=None)
    project_type = models.CharField(max_length=9, choices=ProjectType.choices)
    created_time = models.DateTimeField(auto_now_add=True)
    
class Contributors(models.Model):
    user_id = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    projects_id = models.ForeignKey("api.Projects", on_delete=models.CASCADE)
    
class Issues(models.Model):
    class Priority(models.TextChoices):
        LOW = 'LOW'
        MEDIUM = 'MEDIUM'
        HIGH = 'HIGH'
        
    class IssueType(models.TextChoices):
        BUG = 'BUG'
        FEATURE = 'FEATURE'
        TASK = 'TASK'
        
    class Progress(models.TextChoices):
        TODO = 'To Do'
        IN_PROGRESS = 'In Progress'
        FINISHED = 'Finished'
        
    project_id = models.ForeignKey("api.Projects", on_delete=models.CASCADE)
    author_id = models.ForeignKey("authentication.User", on_delete=models.CASCADE, related_name='issue_author')
    name = models.CharField(max_length=100)
    description = models.TextField(default=None)
    priority = models.CharField(max_length=9, choices=Priority.choices)
    issue_type = models.CharField(max_length=7, choices=IssueType.choices)
    progress = models.CharField(max_length=11, choices=Progress.choices)
    assignment_id = models.ForeignKey("authentication.User", on_delete=models.CASCADE, related_name='assigned_to')
    created_time = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    issue_id = models.ForeignKey("api.Issues", on_delete=models.CASCADE)
    author_id = models.ForeignKey("authentication.User", on_delete=models.CASCADE, related_name='comment_uthor')
    description = models.TextField(default=None)
    created_time = models.DateTimeField(auto_now_add=True)