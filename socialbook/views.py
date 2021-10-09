from django.http import HttpResponse
from django.shortcuts import render
from profiles.models import Profile

def home_view(request):
    user = request.user
    profile = Profile.objects.get_all_profiles_count()

    context = {
        'user': user,
        'profile': profile,
    }

    return render(request, 'home.html', context)