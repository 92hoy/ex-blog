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

            print query

            #rows = cur.fetchall()
            #print rows

        return JsonResponse({'return':'success'})  #Ajax 는  jsonresponse 파일로 받음

    print "hello not ajax"

    return render(request, 'blog.html',{})

def blog_read(request):

    with connections['default'].cursor() as cur:
        query = '''


            SELECT no, title, content, name,
            DATE_FORMAT(resist_date, "%Y-%m-%d %H:%m:%s"),
            DATE_FORMAT(modify_date, "%Y-%m-%d %H:%m:%s")
            FROM one
            order by resist_date asc
        '''  #date_format 검색해서 정규식
        cur.execute(query)

        rows = cur.fetchall()
        print rows

    context = {}

    # context['key'] = 'value'
    # context['hello'] = 333
    # context['test'] = [1,2,3]
    context['rows'] = rows

    return render(request,'blog_read.html',context)

def blog_read_view(request, page):  #(request, 변수)

    print "page = ", page

    with connections['default'].cursor() as cur:
        query = '''


            SELECT no, title, content, name,
            DATE_FORMAT(resist_date, "%Y-%m-%d %H:%m:%s"),
            DATE_FORMAT(modify_date, "%Y-%m-%d %H:%m:%s")
            FROM one
            where no = {page}
        '''.format(page=page)

        print query

        cur.execute(query)

        rows = cur.fetchall()


    context={}

    context['read'] = rows[0]
    return render(request,'blog_read_view.html',context)

def blog_delete (request):

    no = request.GET.get('no')

    print no

    with connections['default'].cursor() as cur:
        query = '''
            delete from one
            where no = {no}
        '''.format(no=no)

        print query

        return JsonResponse({'return':'success', 'no':no})


# def happy_delete(request):
#
#     no = request.GET.get('no')
#
#     print no
#
#     with connections['default'].cursor() as cur:
#             query = '''
#                 delete from one
#                 where no = {no}
#             '''.format(no=no)
#             cur.execute(query)
#
#             print query
#
#
#     return JsonResponse({'return':'success', 'no':no})


# --------------------------------------------------------------------------------------------
# ------------------------------------happy url-----------------------------------------------
# --------------------------------------------------------------------------------------------

def happy(request):

    with connections['default'].cursor() as cur:
        query = '''
            select title, no
            from one
            order by resist_date asc
        '''
        cur.execute(query)

        print query

        rows = cur.fetchall()

    context = {}
    context['rows'] = rows
    return render(request,'happy.html',context)

def happy_save(request):

    input = request.GET.get('input')

    with connections['default'].cursor() as cur:
            query = '''
                insert into one(title, content, name, pw)
                values('{title}','x','x','x')
            '''.format(title=input)
            cur.execute(query)

            print query

    with connections['default'].cursor() as cur:
            query = '''
                select title, no
                from one
                order by resist_date desc
            '''
            cur.execute(query)

            print query

            rows = cur.fetchall()
            title = rows[0][0]
            no = rows[0][1]

    return JsonResponse({'return':'success', 'title':title, 'no':no})

def happy_delete(request):

    no = request.GET.get('no')

    print no

    with connections['default'].cursor() as cur:
            query = '''
                delete from one
                where no = {no}
            '''.format(no=no)
            cur.execute(query)

            print query


    return JsonResponse({'return':'success', 'no':no})


# --------------------------------------------------------------------------------------------
# -----------------------------------------------exer-----------------------------------------
# --------------------------------------------------------------------------------------------


def exer(request):

    with connections['default'].cursor() as cur:
        query = '''
            select title, no, name,
            DATE_FORMAT(resist_date, "%Y-%m-%d %H:%m:%s"),
            DATE_FORMAT(modify_date, "%Y-%m-%d %H:%m:%s")
            from one
            order by resist_date asc
        '''
        cur.execute(query)

        print query

        rows = cur.fetchall()

    context = {}
    context['rows'] = rows

    return render(request,'exer.html',context)

def exer_save(request):

    input1 = request.GET.get('input1')
    input2 = request.GET.get('input2')
    input3 = request.GET.get('input3')
    input4 = request.GET.get('input4')
    print input1
    print input2
    print input3
    print input4

    with connections['default'].cursor() as cur:
            query = '''
                insert into one(title, content, name, pw)
                values('{title}','{content}','{name}','{pw}')
            '''.format(title=input1,content=input2,name=input3, pw=input4)
            cur.execute(query)

            print query


    with connections['default'].cursor() as cur:
            query = '''
                select title, no, content, name
                from one
                order by resist_date desc
            '''
            cur.execute(query)

            print query

            rows = cur.fetchall()

            title = rows[0][0]
            no = rows[0][1]
            content = rows[0][2]
            name =  rows[0][3]

    return JsonResponse({'return':'success', 'title':title, 'no':no,'content':content, 'name':name})

def exer_delete(request):

    no = request.GET.get('no')

    print no

    with connections['default'].cursor() as cur:
            query = '''
                delete from one
                where no = {no}
            '''.format(no=no)
            cur.execute(query)

            print query


    return JsonResponse({'return':'success', 'no':no})

def exer_read(request,page):


    print "page = ", page

    with connections['default'].cursor() as cur:
        query = '''


            SELECT no, title, content, name,
            DATE_FORMAT(resist_date, "%Y-%m-%d %H:%m:%s"),
            DATE_FORMAT(modify_date, "%Y-%m-%d %H:%m:%s")
            FROM one
            where no = {page}
        '''.format(page=page)

        print query

        cur.execute(query)

        rows = cur.fetchall()


    context={}
    context['read'] = rows[0]
    context['aaa'] = page
    return render(request,'exer_read.html',context)



def exer_read_update(request):

    title =request.GET.get('title')
    content =request.GET.get('content')
    no =request.GET.get('no')
    print title
    print content
    print no

    with connections['default'].cursor() as cur:

        query = '''
            update one
            set title = '{title}',content='{content}'
            where no = {no}
        '''.format(title=title, content=content, no=no)
        print query

        cur.execute(query)



        #rows = cur.fetchall() #조회한 테이블 결과 전부

    return JsonResponse({'return':'success','title':title,'content':content,'no':no})



