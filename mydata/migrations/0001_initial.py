# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-25 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programmer_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=50)),
                ('level', models.CharField(choices=[('Junior', 'Junior'), ('Mid_level', 'Mid_level'), ('Senior', 'Senior'), ('Other', 'Other')], default='Junior', max_length=50)),
            ],
        ),
    ]