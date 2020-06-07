from django.shortcuts import render
from apps.blogs.models import Blog


def index(request):
    blogs = Blog.objects.order_by('blog_date')[:3]
    context = {'blogs': blogs}
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')


def services(request):
    return render(request, 'pages/services.html')
