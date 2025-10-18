from django.shortcuts import render
from .models import Profile

def index(request):
    q = request.GET.get('q', '')
    if q:
        profiles = Profile.objects.filter(name__icontains=q) | Profile.objects.filter(city__icontains=q)
    else:
        profiles = Profile.objects.all()
    return render(request, 'profiles/index.html', {'profiles': profiles, 'q': q})
