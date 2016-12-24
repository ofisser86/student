# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


def journal(request):
    return render(request, 'students/journal.html')


def journal_visit(request, sid):
    return HttpResponse('<h1>Journal page for studedent %s</h1>' % sid)


def journal_update(request):
    return HttpResponse('<h1>Journal update page</h1>')