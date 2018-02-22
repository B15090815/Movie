from django.db import models

# Create your models here.
# videoType 代表视频类型0代表电视剧 1代表电影


class Items(models.Model):
    name = models.CharField(max_length=40, blank=True)
    img = models.CharField(max_length=200, blank=True)
    pubdate = models.DateField(default='2017-1-1')
    # videoType = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Links(models.Model):
    # option = models.BooleanField(default=False)
    link = models.TextField()
    # item = models.ForeignKey(Items, related_name="item") #related_name相当于在Items中Links的字段名
