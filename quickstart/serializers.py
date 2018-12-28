#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

@author: dai-wl

@contact: dai-wl@reachauto.com

@file: serializers.py

@time: 2018/12/26 14:10

@desc:

"""
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
