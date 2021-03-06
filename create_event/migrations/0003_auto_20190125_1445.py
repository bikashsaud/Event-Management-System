# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-25 09:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('create_event', '0002_auto_20190125_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_event',
            name='category',
            field=models.CharField(choices=[('Education', 'Education'), ('Fashion', 'Fashion'), ('Food', 'Food'), ('Other', 'Other')], default='Category', max_length=50),
        ),
        migrations.AlterField(
            model_name='create_event',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2019, 1, 25, 9, 0, 33, 700211, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='create_event',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 1, 25, 9, 0, 33, 700211, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='create_event',
            name='type',
            field=models.CharField(choices=[('Fair', 'Fair'), ('Conference', 'Conference'), ('Party', 'Party'), ('Other', 'Other')], default='Types', max_length=50),
        ),
    ]
