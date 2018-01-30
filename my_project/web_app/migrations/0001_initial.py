# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-30 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('email', models.CharField(default='YourName@abc.com', max_length=50)),
                ('employee_id', models.IntegerField()),
            ],
        ),
    ]
