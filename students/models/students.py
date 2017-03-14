# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.


class Student(models.Model):

    class Meta(object):
        verbose_name = "Студент"
        verbose_name_plural = "Студенти"

        # Student Model
    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Ім'я студента"
    )
    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Прізвище'
    )
    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name='Побатькові',
        default=''
    )
    birthday = models.DateField(
        blank=True,
        verbose_name='Дата народження',
        null=True
    )
    student_group = models.ForeignKey(
        'Group',
        verbose_name='Група',
        blank=False,
        null=True,
        on_delete=models.PROTECT
    )
    photo = models.ImageField(
        blank=True,
        verbose_name='Фото',
        null=True
    )
    ticket = models.CharField(
        max_length=256,
        blank=True,
        verbose_name='Білет',
    )
    notes = models.TextField(
        blank=True,
        verbose_name='Додаткові нотатки'
    )

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
