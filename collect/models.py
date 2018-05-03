from django.db import models
from django.contrib.auth.models import User
# import django.utils.timezone as timezone
# Create your models here.
class Experiment(models.Model):
    user = models.ForeignKey(User, related_name='experiment')
    expname = models.CharField(u'实验名称', max_length=30, null=True, blank=True)
    filepath = models.CharField(u'实验文件路径',max_length=500, null=True, blank=True)
    submitdate = models.DateField(u'提交时间', null=True, blank=True)

class Exptemplate(models.Model):
    name = models.CharField(u'实验名称', max_length=30)
    nameformate = models.CharField(u'实验名称格式', max_length=100)
    submitdate = models.DateField(u'截止提交时间', null=True, blank=True)
    isactive = models.BooleanField(u'是否显示',default=True)

    def __str__(self):
        return self.name