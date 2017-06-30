
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from datetime import datetime
from django.utils.translation import ugettext as _

from django.forms import ModelForm
from django.views.generic import UpdateView, DeleteView
from crispy_forms.helper import FormHelper
from  crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from ..util import paginate, get_current_group

from ..models.students import Student
from ..models.groups import Group


def students_list(request):
    current_group = get_current_group(request)
    if current_group:
        students = Student.objects.filter(student_group=current_group)
    else:
        students = Student.objects.all()

    students = students.order_by('last_name')
    # try to order students list

    order_by = request.GET.get('order_by', '')
    if order_by in ('first_name', 'last_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    # paginator students

    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:

        # If page not integer, deliver first page

        students = paginator.page(1)
    except EmptyPage:

        # If page out of range (e.g. 99999), deliver last page of result

        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    # was form posted?
    if request.method == 'POST':
        # was form add button clicked?
        if request.POST.get('add_button') is not None:
            # Errors collection
            errors = {}
            # validate student data will go here
            data = {'middle_name': request.POST.get('middle_name'), 'notes': request.POST.get('notes')}

            # validate user input
            first_name = request.POST.get('first_name', ' ').strip()
            if not first_name:
                errors['first_name'] = _(u"First name field is required")
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', ' ').strip()
            if not last_name:
                errors['last_name'] = _(u"Last name field is required")
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', ' ').strip()
            if not birthday:
                errors['birthday'] = _(u"Birthday field is required")
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = _(u"Enter correct format date (as example 1984-12-30)")
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', ' ').strip()
            if not ticket:
                errors['ticket'] = _(u"Ticket field is required")
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = _(u"Select student group")
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = _(u"Select correct group")
                else:
                    data['student_group'] = groups[0]

            photo = request.FILES.get('photo')
            if photo:
                data['photo'] = photo

                # if not errors:
                #    # create student object
                #     student = Student(
                #         first_name=request.POST['first_name'],
                #         last_name=request.POST['last_name'],
                #         middle_name=request.POST['middle_name'],
                #         birthday=request.POST['birthday'],
                #         ticket=request.POST['ticket'],
                #         student_group=Group.objects.get(pk=request.POST['student_group']),
                #         photo=request.FILES['photo']
                #     )
                # save it to database
            if not errors:
                student = Student(**data)
                student.save()

                # redirect user to students list
                return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('home'), _(u"Student added successfully")))
            else:
                # render form with errors and previous user input
                return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title'),
                                                                      'errors': errors})

        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('home'), _(u"Editing canceled")))
    else:
        # initial form render
        return render(request, "students/students_add.html", {'groups': Group.objects.all().order_by('title')})


class StudentUpdateForm(ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('students_edit', kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # add buttons
        self.helper.layout[-1] = FormActions(Submit('add_button', _(u"Save"), css_class='btn btn-primary'),
                                             Submit('cancel_button', _(u"Cancel"), css_class='btn btn-link'), )


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentUpdateForm
    # fields = '__all__'

    def get_success_url(self):
        return u'%s?status_message=%s' % (reverse('home'), _(u"Student added successfully"))

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('home'), _(u"Editing canceled")))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/students_confirm_delete.html'

    def get_success_url(self):
        return u'%s?status_message=%s' % (reverse('home'), _(u"Student deleted"))