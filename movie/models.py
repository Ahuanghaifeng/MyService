# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class china(models.Model):
    id = models.CharField(max_length=32, default='1', primary_key=True)
    movie_name = models.CharField(max_length=32, default='电影')
    movie_image = models.CharField(max_length=255, null=True)
    movie_abstract = models.CharField(max_length=255, null=True)
    movie_download = models.CharField(max_length=255, null=False)
    movie_time = models.CharField(max_length=32, null=True)

    def __str__(self):
        return self.movie_name
