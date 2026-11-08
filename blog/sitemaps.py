from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import BlogPost


class BlogPostSitemap(Sitemap):
    """Sitemap entries for published blog posts."""

    protocol = "https"
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return BlogPost.objects.all()

    def location(self, post):
        return reverse("blog_detail", kwargs={"slug": post.slug})

    def lastmod(self, post):
        return post.updated_at
