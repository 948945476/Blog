# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-06 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictitle', models.CharField(max_length=50)),
                ('pictxt', models.TextField()),
                ('about', models.TextField()),
            ],
        ),
    ]