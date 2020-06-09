from django.shortcuts import render,get_object_or_404
from .models import Blog
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def index(request):
    blogs = Blog.objects.order_by('blog_date')

    paginator = Paginator(blogs, 6)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)
    context = {'blogs': paged_blogs}
    return render(request, 'blogs/blogs.html', context)


def blog(request, id):
    blog = get_object_or_404(Blog, pk=id)
    context = {'blog': blog}
    return render(request, 'blogs/blog.html', context)


def search(request):
    return render(request, 'blogs/blog.html')
