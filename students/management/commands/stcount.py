from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from students.models import Student, Group


class Command(BaseCommand):
    args = '<model_name model_name ...>'
    help = "Prints to console number of students related objects in a database"

    models = (('student', Student), ('group', Group), ('user', User))

    def handle(self, *args, **options):
        for name, model in self.models:
            # if name in args:
            #     self.stdout.write('Number of %ss in DB = %d' % (name, model.objects.count()))
            self.stdout.write('Number of %ss in DB = %d' % (name, model.objects.count()))