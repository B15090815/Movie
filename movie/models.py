from django.db import models

# Create your models here.


class Items(models.Model):
    name = models.CharField(max_length=30, default='')
    img = models.CharField(max_length=200, default='')
    tag = models.CharField(max_length=80, default='')
    pubdate = models.CharField(max_length=12, default='2017-1-1')
    # category = models.CharField(max_length=40, default='', null=True)

    def __str__(self):
        return self.name


class Links(models.Model):
    link = models.CharField(max_length=800, default='')
    item = models.ForeignKey(Items, related_name='link', on_delete=models.CASCADE)