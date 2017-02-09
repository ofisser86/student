# -*- coding: utf-8 -*-
from django.http import HttpResponse

from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from calendar import monthrange, weekday, day_abbr

from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from ..util import paginate

from ..models import MonthJournal, Student


class JournalView(TemplateView):
    template_name = 'students/journal.html'

    def get_context_data(self, **kwargs):
        # get context data from TemplateView class
        context = super(JournalView, self).get_context_data(**kwargs)

        # check if we need to display some specific month
        if self.request.GET.get('month'):
            month = datetime.strptime(self.request.GET['month'], '%Y-%m-%d').date()
        else:
            today = datetime.today()
            month = date(today.year, today.month, 1)

        # calculate current, previous and next month details;
        # we need this for month navigation element in template
        next_month = month + relativedelta(month=1)
        prev_month = month - relativedelta(month=1)
        context['prev_month'] = prev_month.strftime('%Y-%m-%d')
        context['next_month'] = next_month.strftime('%Y-%m-%d')
        context['year'] = month.year
        context['month_verbose'] = month.strftime('%B')

        # we’ll use this variable in students pagination
        context['cur_month'] = month.strftime('%Y-%m-%d')

        # prepare variable for template to generate
        # journal table header elements
        myear, mmonth = month.year, month.month
        number_of_days = monthrange(myear, mmonth)[1]
        context['month_header'] = [{'day': d,
                                    'verbose': day_abbr[weekday(myear, mmonth, d)][:2]}
                                   for d in range(1, number_of_days + 1)

                                   ]

        # url to update student presence, for form post
        queryset = Student.objects.all().order_by('last_name')

        # це адреса для посту AJAX запиту, як бачите, ми
        # робитимемо його на цю ж в’юшку; в’юшка журналу
        # буде і показувати журнал і обслуговувати запити
        # типу пост на оновлення журналу;

        update_url = reverse('journal')

        # go over all students and collect data about presence
        # during selected month
        students = []
        for student in queryset:
            # try to get journal object by month selected
            # month and current student
            try:
                journal = MonthJournal.objects.get(student=student, date=month)
            except Exception:
                journal = None

            # fill in days presence list for current student
            days = []
            for day in range(1, number_of_days + 1):
                days.append({
                    'day': day,
                    'present': journal and getattr(journal, 'present_day%d' % day, False) or False,
                    'date': date(myear, mmonth, day).strftime('%Y-%m-%d'),
                            })

            # prepare metadata for current student

            students.append({
                'fullname': u'%s %s' % (student.last_name, student.first_name),
                'day': days,
                'id': student.id,
                'update_url': update_url,
            })

            # apply pagination, 10 students per page
            context = paginate(students, 10, self.request, context, var_name='students')

            # повертаємо оновлений словник із даними
            return context


def journal_visit(request, sid):
    return HttpResponse('<h1>Journal page for studedent %s</h1>' % sid)


def journal_update(request):
    return HttpResponse('<h1>Journal update page</h1>')
