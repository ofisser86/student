# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


def groups_list(request):
    groups = (
        {
            'id': 1,
            'group_name': 'МтМ-21',
            'group_lider': {'id': 1, 'name': 'Сергій Притула'}},
        {
            'id': 2,
            'group_name': 'МтМ-22',
            'group_lider': {'id': 2, 'name': 'Дмитро Дубілет'}},
        {
            'id': 3,
            'group_name': 'МтМ-23',
            'group_lider': {'id': 3, 'name': 'Оксана Варнава'}
        },

    )
    return render(request, 'students/groups_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Groups Listing</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Groups Listing %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Groups Listing %s</h1>' % gid)