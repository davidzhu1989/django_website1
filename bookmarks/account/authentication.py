#!/usr/bin/env python  
# coding=utf-8
__author__ = 'Boaz'
# @Time : 2019/4/3 15:59 

# 邮箱验证而已

from django.contrib.auth.models import User


class EmailAuthBackend:
    """
    Authenticate using an e-mail address
    """
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None