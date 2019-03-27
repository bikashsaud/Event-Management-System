# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-25 05:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('create_event', '0014_auto_20190128_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_event',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 25, 5, 58, 5, 253231, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='create_event',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 25, 5, 58, 5, 253231, tzinfo=utc)),
        ),
    ]
