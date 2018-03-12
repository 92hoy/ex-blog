 # -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connections
from django.utils import timezone
import datetime


def index(request):

    if request.is_ajax():

        title = request.GET.get('title')
        content = request.GET.get('content')
        name = request.GET.get('name')
        pw = request.GET.get('pw')


        print title
        print content
        print name
        print pw

        with connections['default'].cursor() as cur:
            query = '''
                insert into one(title, content, name, pw)
                values('{title}','{content}','{name}','{pw}')
            '''.format(title=title, content=content, name=name, pw=pw)
            cur.execute(query)

            rows = cur.fetchall()
            print rows

        return JsonResponse({'return':'success'})

    print "hello not ajax"

    return render(request, 'blog.html',{})

def blog_read(request):

    return render(request,'blog_read.html',{})

