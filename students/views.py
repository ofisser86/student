# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Views for students


def students_list(request):
    students = (
        {
            'id': 1,
            'first_name': 'Віталій',
            'last_name': 'Подоба',
            'ticket': 213,
            'img': 'img/podoba3.jpg'},
        {
            'id': 2,
            'first_name': 'Корост',
            'last_name': 'Андрій',
            'ticket': 111,
            'img': 'img/me.jpeg'},
        {
            'id': 3,
            'first_name': 'Притула',
            'last_name': 'Тарас',
            'ticket': 515,
            'img': 'img/piv.png'},

    )
    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Student Edit Form %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Student Delete Form %s </h1>' % sid)

# Views for Groups


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


