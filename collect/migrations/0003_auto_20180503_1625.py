# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-05-03 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0002_auto_20180427_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='exptemplate',
            name='isactive',
            field=models.BooleanField(default=True, verbose_name='是否显示'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='submitdate',
            field=models.DateField(blank=True, null=True, verbose_name='提交时间'),
        ),
    ]