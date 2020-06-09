from django.shortcuts import render, get_object_or_404
from .models import Project
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def index(request):
    projects = Project.objects.order_by('project_date')
    paginator = Paginator(projects, 3)
    page = request.GET.get('page')
    paged_projects = paginator.get_page(page)
    context = {'projects': paged_projects}
    return render(request, 'projects/projects.html', context)


def project(request, id):
    project = get_object_or_404(Project, pk=id)
    context = {'project': project}
    return render(request, 'projects/project.html', context)


def search(request):
    return render(request, 'projects/projects.html')
