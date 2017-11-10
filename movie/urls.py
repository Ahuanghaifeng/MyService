# encoding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    # ^$约束空字符串 ^index/$分号很重要
    url(r'^index', views.movie_index),
    url(r'^china', views.movie_china),
    url(r'^japan', views.movie_japan),
    url(r'^america', views.movie_america),
    url(r'^detail', views.movie_detail)
    # url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    # url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name="edit_page"),
    # url(r'^edit_action/$', views.edit_action, name="edit_action"),
    # url(r'^index', views.index),
    # url(r'^article_detail/(?P<article_id>[0-9]+)$',views.article_page)

]
