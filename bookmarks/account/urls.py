# coding=utf-8
# !/usr/bin/env python
__author__ = 'Boaz'
# @Time : 2019/4/3 0:13 

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # path('login/', views.user_login, name='login'),
    # 使用系统自带的登录和登出视图
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name="dashboard")
]