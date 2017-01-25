# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.


class Exam(models.Model):

    class Meta(object):
        verbose_name = "Іспит"
        verbose_name_plural = "Іспити"

        # Exam
    subject_title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Назва предмету"
    )
    teacher = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Ім'я викладача"
    )
    exam_group = models.ForeignKey(
        'Group',
        blank=True,
        null=True,
        verbose_name='Група',
        on_delete=models.SET_NULL
    )
    exam_date = models.DateField(
        blank=True,
        verbose_name='Дата екзамену',
        null=True
    )
    note = models.TextField(
        blank=True,
        verbose_name='Додаткові нотатки'
    )

    def __unicode__(self):
        if self.exam_group:
            return "%s (%s )" % (self.subject_title, self.exam_group.title)
        else:
            return "%s" % self.subject_title
