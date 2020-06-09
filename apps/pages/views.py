from django.shortcuts import render
from apps.blogs.models import Blog
from apps.projects.models import Project


def index(request):
    blogs = Blog.objects.order_by('blog_date')[:3]
    projects = Project.objects.order_by('project_date')[:4]
    context = {'blogs': blogs, 'projects': projects}
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')


def services(request):
    return render(request, 'pages/services.html')
