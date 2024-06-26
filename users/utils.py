from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from users.models import Skill, Profile
from django.db.models import Q
from django.core.handlers.wsgi import WSGIRequest


def paginate_profiles(request: WSGIRequest, profiles, result_range) -> tuple:
    page = request.GET.get('page')
    results = result_range
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    left_idx = (int(page) - 4)
    if left_idx < 1:
        left_idx = 1

    right_idx = (int(page) + 5)
    if right_idx >= paginator.num_pages:
        right_idx = paginator.num_pages

    custom_range = range(left_idx, right_idx + 1)
    return custom_range, profiles


def search_profiles(request: WSGIRequest) -> tuple:
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    skills = Skill.objects.filter(name__icontains=search_query)
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills))
    return profiles, search_query
