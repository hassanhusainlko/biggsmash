from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView, TemplateView

from blog.sitemaps import BlogPostSitemap
from core.sitemaps import StaticViewSitemap
from services import views as services_views
from services.sitemaps import ServiceSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'services': ServiceSitemap,
    'blog': BlogPostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='sitemap',
    ),
    path(
        'robots.txt',
        TemplateView.as_view(template_name='robots.txt', content_type='text/plain'),
        name='robots_txt',
    ),
    path('', include('home.urls')),
    path('services/', include('services.urls')),
    path('events/', services_views.events, name='events'),
    path('about/', include('about.urls')),
    path('blog/', include('blog.urls')),
    path('career/', include('career.urls')),
    path('contact/', include('contact.urls')),

    # Legacy .html links from the original static UI design.
    path('index.html', RedirectView.as_view(pattern_name='home', permanent=True)),
    path('about.html', RedirectView.as_view(pattern_name='about', permanent=True)),
    path('services.html', RedirectView.as_view(pattern_name='services_list', permanent=True)),
    path('events.html', RedirectView.as_view(pattern_name='events', permanent=True)),
    path('careers.html', RedirectView.as_view(pattern_name='career', permanent=True)),
    path('blog.html', RedirectView.as_view(pattern_name='blog_list', permanent=True)),
    path('contact.html', RedirectView.as_view(pattern_name='contact', permanent=True)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
