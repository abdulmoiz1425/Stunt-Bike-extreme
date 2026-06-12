from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.blog.models import Article


class StaticViewSitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return [
            'home', 'about', 'privacy', 'terms', 'disclaimer', 'cookie_policy',
            'blog', 'contact', 'old_versions',
            'mod_apk', 'for_pc', 'for_ios', 'for_smart_tv', 'for_tv_box',
        ]

    def location(self, item):
        return reverse(item)


class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Article.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.publish_date

    def location(self, obj):
        return reverse('article_detail', args=[obj.slug])
