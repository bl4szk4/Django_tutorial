from django.db.models import Q
from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from projects.models import Tag, Project


def paginate_projects(request: WSGIRequest, projects, result_range) -> tuple:
    page = request.GET.get('page')
    results = result_range
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    left_idx = (int(page) - 4)
    if left_idx < 1:
        left_idx = 1

    right_idx = (int(page) + 5)
    if right_idx >= paginator.num_pages:
        right_idx = paginator.num_pages

    custom_range = range(left_idx, right_idx + 1)
    return custom_range, projects


def search_projects(request: WSGIRequest) -> tuple:
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )
    return projects, search_query
