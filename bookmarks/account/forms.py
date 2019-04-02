# coding=utf-8
# !/usr/bin/env python
__author__ = 'Boaz'
# @Time : 2019/4/2 23:59 

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
