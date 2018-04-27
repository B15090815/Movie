from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Member(models.Model):
#     gender_choice = (
#         (u'男',u'男'),
#         (u'女',u'女'),
#     )
#     supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="member", null=True, blank=True)
#     name = models.CharField(u'姓名', max_length=32)
#     gender = models.CharField(u'性别', choices=gender_choice, max_length=2)
#     birthdate = models.DateField(u'出生日期', auto_now=False)
#     height = models.FloatField(u'身高(cm)')
#     weight = models.FloatField(u'体重(kg)')

#     def __str__(self):
#         return self.name

# class MonitorData(models.Model):
#     owner = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="data", null=True, blank=True)
#     longitude = models.FloatField(u'经度')
#     latitude = models.FloatField(u'经度')
#     tempature = models.FloatField(u'温度')
#     heart_rate = models.PositiveIntegerField(u'心率')
#     oxygen_saturation = models.FloatField(u'血氧饱和度')
#     position_x = models.FloatField(u'人体姿态x参数')
#     position_y = models.FloatField(u'人体姿态y参数')
#     position_z = models.FloatField(u'人体姿态z参数')
#     time = models.TimeField(u'记录创建时间', auto_now_add=True)


class Temperature(models.Model):
    msg = models.CharField(u'状态信息',max_length=50)
    signature = models.CharField(u'签名', max_length=500)
    info = models.CharField(u'数据', max_length=1000)