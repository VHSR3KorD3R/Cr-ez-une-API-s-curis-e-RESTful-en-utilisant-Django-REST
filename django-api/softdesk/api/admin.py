from django.contrib import admin
from api.models import Projects, Contributors, Issues, Comments


class ContributorsAdmin(admin.TabularInline):
    model = Projects.contributors.through

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('author_id', 'get_name')
    fieldsetsinlines = [
        (None, {'fields':['author_id', 'name', 'description', 'project_type', 'created_time']})
    ]
    
    inlines = (ContributorsAdmin,)
    
    def get_name(self, obj):
        return [contributor.username for contributor in obj.contributors.all()]

class IssuesAdmin(admin.ModelAdmin):
    pass

class CommentsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Issues, IssuesAdmin)
admin.site.register(Comments, CommentsAdmin)
