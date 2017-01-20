# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models.groups import Group


def groups_list(request):
    groups = Group.objects.all()
    groups = groups.order_by('title')
    # try to order students list

    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    # paginator students

    paginator = Paginator(groups, 3)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:

        # If page not integer, deliver first page

        groups = paginator.page(1)
    except EmptyPage:

        # If page out of range (e.g. 99999), deliver last page of result

        groups = paginator.page(paginator.num_pages)

    return render(request, 'students/groups_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Groups Listing</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Groups Listing %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Groups Listing %s</h1>' % gid)