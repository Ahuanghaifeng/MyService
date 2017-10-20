#encoding=utf-8
from __future__ import unicode_literals
from django.db import models


class Article(models.Model):
    # 博客标题定义为字符串，最大长度为32默认值是title

    title = models.CharField(max_length=32, default='Title')
    author = models.CharField(null=True, max_length=16)
    image_url = models.CharField(max_length=255, null=True)
    abstract = models.TextField(null=True)
    # 定义blog的内容，内容可以为空
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(null=True)
    state = models.IntegerField(default=0) #0表示一般文章，1表示推荐

    def __str__(self):
        return self.title
