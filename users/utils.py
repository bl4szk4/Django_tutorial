from users.models import Skill, Profile
from django.db.models import Q
from django.core.handlers.wsgi import WSGIRequest


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
