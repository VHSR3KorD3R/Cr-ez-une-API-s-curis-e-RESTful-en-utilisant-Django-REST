from django.contrib import admin
from api.models import Projects, Contributors, Issues, Comments


# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):
    #list_display = ('author_id', 'name')
    pass

class ContributorsAdmin(admin.ModelAdmin):
    pass

class IssuesAdmin(admin.ModelAdmin):
    pass

class CommentsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Contributors, ContributorsAdmin)
admin.site.register(Issues, IssuesAdmin)
admin.site.register(Comments, CommentsAdmin)
