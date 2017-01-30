# from .settings import PORTAL_URL
#from students.views.students import students_list
#from django.http import HttpRequest


def students_proc(request):
    PORTAL_URL = '{0}://{1}'.format(request.scheme, request.get_host())
    return {'PORTAL_URL': PORTAL_URL}
