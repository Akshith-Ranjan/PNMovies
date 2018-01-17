# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template import loader
import json

# Create your views here.

from django.http import HttpResponse
from .models import Movies,Credits

def index(request):
    if request.GET.get('search', ''):
        search = request.GET.get('search', '')
        obj = Movies.objects.filter(title__contains=search)
        context = {'obj': obj}
        return render(request, 'movies/index.html', context)
    elif request.GET.get('mid', ''):
        mid = request.GET.get('mid', '')
        obj1 = Credits.objects.filter(mid=mid)[0]
        a= str(obj1.title)
        st = obj1.cast
        obj1 = json.loads(str(st))
        context = {'obj1': obj1,'a':a}
        return render(request, 'movies/index.html', context)
    elif request.GET.get('cid', ''):
        cid = request.GET.get('cid', '')
        cname = request.GET.get('cname', '')
        m = ': '+cid+','
        obj2 = Credits.objects.filter(cast__contains=cname)
        context = {'obj2': obj2,'cname':cname}
        return render(request, 'movies/index.html', context)
    else:
        return render(request, 'movies/index.html' )

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
