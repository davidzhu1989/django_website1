#!/usr/bin/env python
# @Time : 2019/3/29 14:06 
__author__ = 'Boaz'

from django.urls import path
from .import views


app_name = 'blog'
urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='post_detail'),
]