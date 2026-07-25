from django.shortcuts import render, get_object_or_404
from .data import get_all_services, get_service

def services_list(request):
    services = get_all_services()
    return render(request, 'services/index.html', {'services': services})

def service_detail(request, slug):
    service = get_service(slug)
    if not service:
        return render(request, '404.html', status=404)
    return render(request, 'services/detail.html', {'service': service, 'slug': slug})
