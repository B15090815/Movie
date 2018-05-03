# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-04-27 14:57
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
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expname', models.CharField(blank=True, max_length=30, null=True, verbose_name='实验名称')),
                ('filepath', models.CharField(blank=True, max_length=500, null=True, verbose_name='实验文件路径')),
                ('submitdate', models.DateField(auto_now_add=True, verbose_name='提交时间')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='experiment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exptemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='实验名称')),
                ('nameformate', models.CharField(max_length=100, verbose_name='实验名称格式')),
                ('submitdate', models.DateField(blank=True, null=True, verbose_name='截止提交时间')),
            ],
        ),
    ]