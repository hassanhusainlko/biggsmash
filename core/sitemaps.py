from django.contrib.sitemaps import Sitemap
from django.urls import reverse

# (url name, priority, changefreq)
STATIC_PAGES = [
    ("home", 1.0, "weekly"),
    ("about", 0.6, "monthly"),
    ("services_list", 0.9, "monthly"),
    ("events", 0.7, "monthly"),
    ("blog_list", 0.8, "daily"),
    ("career", 0.6, "weekly"),
    ("contact", 0.6, "monthly"),
]


class StaticViewSitemap(Sitemap):
    """Sitemap entries for the site's main, non-model pages."""

    protocol = "https"

    def items(self):
        return STATIC_PAGES

    def location(self, item):
        return reverse(item[0])

    def priority(self, item):
        return item[1]

    def changefreq(self, item):
        return item[2]
