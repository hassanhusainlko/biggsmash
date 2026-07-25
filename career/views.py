from django.shortcuts import render
from .models import JobPosting

def career(request):
    jobs = JobPosting.objects.filter(is_active=True)
    return render(request, 'career/index.html', {'jobs': jobs})
