# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='americamovie',
            fields=[
                ('id', models.CharField(default='1', max_length=32, primary_key=True, serialize=False)),
                ('movie_name', models.CharField(default='\u7535\u5f71', max_length=32)),
                ('movie_image', models.CharField(max_length=255, null=True)),
                ('movie_abstract', models.CharField(max_length=255, null=True)),
                ('movie_download', models.CharField(max_length=255)),
                ('movie_time', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='japanmovie',
            fields=[
                ('id', models.CharField(default='1', max_length=32, primary_key=True, serialize=False)),
                ('movie_name', models.CharField(default='\u7535\u5f71', max_length=32)),
                ('movie_image', models.CharField(max_length=255, null=True)),
                ('movie_abstract', models.CharField(max_length=255, null=True)),
                ('movie_download', models.CharField(max_length=255)),
                ('movie_time', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='newmovie',
            fields=[
                ('id', models.CharField(default='1', max_length=32, primary_key=True, serialize=False)),
                ('movie_name', models.CharField(default='\u7535\u5f71', max_length=32)),
                ('movie_image', models.CharField(max_length=255, null=True)),
                ('movie_abstract', models.CharField(max_length=255, null=True)),
                ('movie_download', models.CharField(max_length=255)),
                ('movie_time', models.CharField(max_length=32, null=True)),
            ],
        ),
    ]
