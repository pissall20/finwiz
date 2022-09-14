from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticSitemap(Sitemap):

    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return ['index', 'contact_us', 'about', 'privacy', 'disclaimer']

    def location(self, item):
        return reverse(item)
