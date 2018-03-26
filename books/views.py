# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# Create your views here.
def index(request):
    return HttpResponseRedirect('www.huanghaifeng.top:8088')
