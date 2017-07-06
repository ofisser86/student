from django.core.management.base import BaseCommand

from students.models import Student


class Command(BaseCommand):
    args = '<model_name model_name ...>'
    help = "Prints to console number of students related objects in a database"

    def handle(self, *args, **options):
        if 'student' in args:
            self.stdout.write('Number of student in DB = %d' % Student.objects.count())
