# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.


class Group(models.Model):

    class Meta(object):
        verbose_name = "Група"
        verbose_name_plural = "Групи"

        # Group Model
    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Назва групи"
    )
    leader = models.OneToOneField(
        'Student',
        blank=True,
        null=True,
        verbose_name='Староста',
        on_delete=models.SET_NULL
    )
    note = models.TextField(
        blank=True,
        verbose_name='Додаткові нотатки'
    )

    def __unicode__(self):
        if self.leader:
            return "%s (%s %s)" % (self.title, self.leader.first_name, self.leader.last_name)
        else:
            return "%s" % self.title
