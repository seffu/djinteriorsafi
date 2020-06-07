from django.contrib import admin

from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'blog_date')
    list_display_links = ('id', 'author', 'title')
    search_fields = ('id', 'author', 'title', 'blog_date')
    list_per_page = 25

admin.site.register(Blog,BlogAdmin)
