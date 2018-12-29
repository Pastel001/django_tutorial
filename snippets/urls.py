#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

@author: dai-wl

@contact: dai-wl@reachauto.com

@file: urls.py

@time: 2018/12/28 9:43

@desc:

"""
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from snippets import views_api_view
from snippets import views_class_view
from snippets import views_class_mixins_view

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]

urlpatterns = [
    url(r'^snippets/$', views_api_view.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views_api_view.snippet_detail),
]

urlpatterns = [
    url(r'^snippets/$', views_class_view.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views_class_view.SnippetDetail.as_view()),
]

urlpatterns = [
    url(r'^snippets/$', views_class_mixins_view.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views_class_mixins_view.SnippetDetail.as_view()),
    url(r'^users/$', views_class_mixins_view.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views_class_mixins_view.UserDetail.as_view()),
    url(r'^$', views_class_mixins_view.api_root),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views_class_mixins_view.SnippetHighlight.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^$', views_class_mixins_view.api_root),
    url(r'^snippets/$',
        views_class_mixins_view.SnippetList.as_view(),
        name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$',
        views_class_mixins_view.SnippetDetail.as_view(),
        name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        views_class_mixins_view.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    url(r'^users/$',
        views_class_mixins_view.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views_class_mixins_view.UserDetail.as_view(),
        name='user-detail')
])

# 可浏览API的登录和注销视图
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
