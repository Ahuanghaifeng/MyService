# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='china',
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
