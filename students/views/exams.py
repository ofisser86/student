from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models.exams import Exam


def exams_list(request):
    exams = Exam.objects.all()
    exams = exams.order_by('subject_title')
    # try to order students list

    order_by = request.GET.get('order_by', '')
    if order_by in ('exams', 'date'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()

    # paginator groups

    paginator = Paginator(exams, 3)
    page = request.GET.get('page')
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:

        # If page not integer, deliver first page

        exams = paginator.page(1)
    except EmptyPage:

        # If page out of range (e.g. 99999), deliver last page of result

        exams = paginator.page(paginator.num_pages)

    return render(request, 'students/exams.html', {'exams': exams})


def exams_add(request):
    return HttpResponse('<h1>Exam add</h1>')


def exams_edit(request, eid):
    return HttpResponse('<h1>Exam edit %s</h1>' % eid)


def exams_delete(request, eid):
    return HttpResponse('<h1>Delete exam %s</h1>' % eid)