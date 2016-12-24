# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


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