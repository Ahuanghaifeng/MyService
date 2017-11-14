# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from . import models
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# Create your views here.
def movie_index(request):
    from movie.pager import Pagination
    # pk 是Primary key主键的意思即为文章id
    movie = models.newmovie.objects.all()
    page = request.GET.get('p')  #接收网页中的page值
    page_obj = Pagination(len(movie), page)
    print page
    print page_obj.start()
    movies = movie[page_obj.start():page_obj.end()]
    return render(request, 'movie/index.html', {'movies': movies,'page_obj':page_obj, 'type': '0'})

def movie_china(request):
    from movie.pager import Pagination
    # pk 是Primary key主键的意思即为文章id
    movie = models.china.objects.all()
    page = request.GET.get('p')  # 接收网页中的page值
    page_obj = Pagination(len(movie), page)
    print page
    print page_obj.start()
    movies = movie[page_obj.start():page_obj.end()]
    return render(request, 'movie/index.html', {'movies': movies, 'page_obj': page_obj,'type': '1'})

def movie_japan(request):
    from movie.pager import Pagination
    # pk 是Primary key主键的意思即为文章id
    movie = models.japanmovie.objects.all()
    page = request.GET.get('p')  # 接收网页中的page值
    page_obj = Pagination(len(movie), page)
    print page
    print page_obj.start()
    movies = movie[page_obj.start():page_obj.end()]
    return render(request, 'movie/index.html', {'movies': movies, 'page_obj': page_obj,'type': '2'})

def movie_america(request):
    from movie.pager import Pagination
    # pk 是Primary key主键的意思即为文章id
    movie = models.americamovie.objects.all()
    page = request.GET.get('p')  # 接收网页中的page值
    page_obj = Pagination(len(movie), page)
    print page
    print page_obj.start()
    movies = movie[page_obj.start():page_obj.end()]
    return render(request, 'movie/index.html', {'movies': movies, 'page_obj': page_obj,'type': '3'})

def movie_detail(request):
    movie_id = request.GET.get('id')
    tp = request.GET.get('type')
    img = ''
    if tp == '0':
        movie = models.newmovie.objects.get(pk=movie_id)
        img = models.newmovie.objects.filter(pk=movie_id).values("movie_image")
    elif tp == '1':
        movie = models.china.objects.get(pk=movie_id)
        img = models.china.objects.filter(pk=movie_id).values("movie_image")
    elif tp == '2':
        movie = models.japanmovie.objects.get(pk=movie_id)
        img = models.japanmovie.objects.filter(pk=movie_id).values("movie_image")
    elif tp == '3':
        movie = models.americamovie.objects.get(pk=movie_id)
        img = models.americamovie.objects.filter(pk=movie_id).values("movie_image")
    imgs = list(img)
    dictimg = imgs[0]
    imageurl = dictimg['movie_image']
    print imageurl
    if ',' in imageurl:
        image1 = imageurl.split(',')[0]
        image2 = imageurl.split(',')[1]
        return render(request, "movie/detail.html", {'movie': movie,'image1':image1,'image2':image2})
    else:
        image1 = imageurl
        return render(request, "movie/detail.html", {'movie': movie,'image1':image1})


