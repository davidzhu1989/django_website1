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
    path('', views.dashboard, name="dashboard"),
    # passwordChangeView 渲染修改密码的页面和表单
    path('password_change', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # change_done表示修改密码成功后显示消息
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    # 重置密码视图
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_complete"),
]