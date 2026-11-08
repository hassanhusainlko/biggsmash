from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .data import SERVICES


class ServiceSitemap(Sitemap):
    """Sitemap entries for each service detail page."""

    protocol = "https"
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return list(SERVICES)

    def location(self, slug):
        return reverse("service_detail", kwargs={"slug": slug})
