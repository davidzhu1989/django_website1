#!/usr/bin/env python
# @Time : 2019/3/31 23:03 
__author__ = 'Boaz'

from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated