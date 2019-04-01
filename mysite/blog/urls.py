#!/usr/bin/env python
# @Time : 2019/3/29 14:06 
__author__ = 'Boaz'

from django.urls import path
from . import views
from .feed import LatestPostFeed

app_name = 'blog'
urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>', views.post_list, name="post_list_by_tag"),
    path('feed/', LatestPostFeed(), name='post_feed'),
    path('search/', views.post_search,name='post_search')
]