# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-03-17 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20180316_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='links',
            name='link',
            field=models.CharField(default='', max_length=1500),
        ),
    ]
