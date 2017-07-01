"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from students.views import students, groups, journal, exams, contact_admin
from students.views.students import StudentUpdateView, StudentDeleteView
from students.views.journal import JournalView
from students.views.set_language import set_language
from django.views.i18n import JavaScriptCatalog
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from .settings import MEDIA_ROOT, DEBUG
if settings.DEBUG:
    import debug_toolbar

urlpatterns = [
    # Students urls
    url(r'^$', students.students_list, name='home'),

    url(r'^students/add/$', students.students_add, name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),

    # Groups url

    url(r'^groups/$', groups.groups_list, name='groups_list'),
    url(r'^groups/add/$', groups.groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', groups.groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', groups.groups_delete, name='groups_delete'),

    # Journal url

    url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),
    url(r'^journal/update', journal.journal_update, name='update'),

    # Exam url
    url(r'^exams/$', exams.exams_list, name='exams'),
    url(r'^exams/add/$', exams.exams_add, name='exams_add'),
    url(r'^exams/(?P<eid>\d+)/edit/$', exams.exams_edit, name='exam_edit'),
    url(r'^exams/(?P<eid>\d+)/delete/$', exams.exams_delete, name='delete'),

    # Form contact admin

    url(r'^contact-admin/$', contact_admin.contact_admin, name='contact_admin'),
    # Form contact with used django-contact-form
    # url(r'^contact/', include('contact_form.urls')),

    url(r'^admin/', admin.site.urls),

    # Debug toolbar

    url(r'^__debug__/', include(debug_toolbar.urls)),

    # Translate

    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^set-language/$',  set_language, name='set_language'),
    # serve files from media folder

    # User Related urls
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page':'home'}, name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'), name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls', namespace='users'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
