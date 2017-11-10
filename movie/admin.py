# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'movie_download', 'movie_time')
    list_filter = ('movie_name',)


admin.site.register(models.china, MovieAdmin)