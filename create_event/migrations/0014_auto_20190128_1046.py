# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-28 05:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('create_event', '0013_auto_20190128_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_event',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2019, 1, 28, 5, 1, 1, 653375, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='create_event',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 1, 28, 5, 1, 1, 653375, tzinfo=utc)),
        ),
    ]
