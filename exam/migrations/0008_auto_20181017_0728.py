# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-10-17 07:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_exam_creation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Exam_creation',
            new_name='creation',
        ),
    ]
