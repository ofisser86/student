from .settings import PORTAL_URL
from students.views.students import students_list


def students_proc(request):
    return {'PORTAL_URL': PORTAL_URL}
