# encoding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    # ^$约束空字符串 ^index/$分号很重要
    url(r'^$', views.blog_index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name="edit_page"),
    url(r'^edit_action/$', views.edit_action, name="edit_action"),
    url(r'^index', views.index)

]
