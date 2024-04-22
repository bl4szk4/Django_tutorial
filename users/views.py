from django.shortcuts import render
from .models import Profile
# Create your views here.


def profiles(request):
    profiles = Profile.objects.all()
    return render(request, r'users\profiles.html', {'profiles': profiles})


def userProfile(request, pk):
    profile = Profile.objects.get(pk=pk)

    skill_with_description = profile.skill_set.exclude(description__iexact='')
    other_skills = profile.skill_set.filter(description='')
    context = {'profile': profile, 'skill_with_description': skill_with_description, 'other_skills': other_skills}
    return render(request, r'users\user-profile.html', context)
