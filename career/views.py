from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import JobApplicationForm
from .models import JobPosting


def career(request):
    jobs = JobPosting.objects.filter(is_active=True)
    return render(request, 'career/index.html', {'jobs': jobs})


def apply(request, job_id=None):
    job = None
    if job_id is not None:
        job = get_object_or_404(JobPosting, pk=job_id, is_active=True)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            role = job.title if job else 'the role you applied for'
            messages.success(
                request,
                f'Thank you, {application.name}! Your application for {role} '
                'has been received. Our team will get in touch with you soon.',
            )
            return redirect('career')
    else:
        form = JobApplicationForm()

    return render(request, 'career/apply.html', {'form': form, 'job': job})
