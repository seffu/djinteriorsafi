from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'location', 'project_date')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'location', 'project_date')
    list_per_page = 25

admin.site.register(Project, ProjectAdmin)
