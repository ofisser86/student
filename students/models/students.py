from __future__ import unicode_literals
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Student(models.Model):

    class Meta(object):
        verbose_name = _("Student")
        verbose_name_plural = _("Students")

        # Student Model
    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_("First name")
    )
    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_("Last name")
    )
    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=_("Middle name"),
        default=''
    )
    birthday = models.DateField(
        blank=True,
        verbose_name=_("Date of birth"),
        null=True
    )
    student_group = models.ForeignKey(
        'Group',
        verbose_name=_("Group"),
        blank=False,
        null=True,
        on_delete=models.PROTECT
    )
    photo = models.ImageField(
        blank=True,
        verbose_name=_("Photo"),
        null=True
    )
    ticket = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=_("Ticket"),
    )
    notes = models.TextField(
        blank=True,
        verbose_name=_("Extra notes")
    )

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)