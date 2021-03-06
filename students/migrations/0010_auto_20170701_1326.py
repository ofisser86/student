# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-01 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20170314_1312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Date of birth'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=256, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=256, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='Middle name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Extra notes'),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='students.Group', verbose_name='Group'),
        ),
        migrations.AlterField(
            model_name='student',
            name='ticket',
            field=models.CharField(blank=True, max_length=256, verbose_name='Ticket'),
        ),
    ]
