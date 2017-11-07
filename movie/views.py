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
    movie = models.china.objects.all()
    page = request.GET.get('p')  #接收网页中的page值
    page_obj = Pagination(len(movie), page)
    print page
    print page_obj.start()
    movies = movie[page_obj.start():page_obj.end()]
    return render(request, 'movie/index.html', {'movies': movies,'page_obj':page_obj})
