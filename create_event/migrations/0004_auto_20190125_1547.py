# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-25 10:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('create_event', '0003_auto_20190125_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_event',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2019, 1, 25, 10, 2, 40, 116815, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='create_event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='events/'),
        ),
        migrations.AlterField(
            model_name='create_event',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 1, 25, 10, 2, 40, 116815, tzinfo=utc)),
        ),
    ]