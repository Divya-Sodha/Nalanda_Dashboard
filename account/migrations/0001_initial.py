# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-25 10:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('topic_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=140)),
                ('content_id', models.CharField(max_length=32)),
                ('channel_id', models.CharField(max_length=32)),
                ('total_questions', models.IntegerField()),
                ('sub_topics', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LatestFetchDate',
            fields=[
                ('date_id', models.AutoField(primary_key=True, serialize=False)),
                ('latest_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MasteryLevelClass',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('content_id', models.CharField(max_length=32)),
                ('channel_id', models.CharField(max_length=32)),
                ('date', models.DateTimeField()),
                ('completed_questions', models.IntegerField(default=0)),
                ('correct_questions', models.IntegerField(default=0)),
                ('attempt_questions', models.IntegerField(default=0)),
                ('students_completed', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MasteryLevelSchool',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('content_id', models.CharField(max_length=32)),
                ('channel_id', models.CharField(max_length=32)),
                ('date', models.DateTimeField()),
                ('completed_questions', models.IntegerField(default=0)),
                ('correct_questions', models.IntegerField(default=0)),
                ('attempt_questions', models.IntegerField(default=0)),
                ('students_completed', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MasteryLevelStudent',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('content_id', models.CharField(max_length=32)),
                ('channel_id', models.CharField(max_length=32)),
                ('date', models.DateTimeField()),
                ('completed_questions', models.IntegerField(default=0)),
                ('correct_questions', models.IntegerField(default=0)),
                ('attempt_questions', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfoClass',
            fields=[
                ('class_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=60)),
                ('parent', models.BigIntegerField()),
                ('total_students', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfoSchool',
            fields=[
                ('school_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=60)),
                ('total_students', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfoStudent',
            fields=[
                ('student_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=60)),
                ('parent', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRoleCollectionMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.UserInfoClass')),
                ('institute_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.UserInfoSchool')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='masterylevelstudent',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.UserInfoStudent'),
        ),
        migrations.AddField(
            model_name='masterylevelschool',
            name='school_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.UserInfoSchool'),
        ),
        migrations.AddField(
            model_name='masterylevelclass',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.UserInfoClass'),
        ),
    ]
