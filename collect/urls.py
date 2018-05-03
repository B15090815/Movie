from django.conf.urls import url
from collect.views import *


urlpatterns = [
    url(r'^$',index),
    url(r'login/$',login, name="login"),
    url(r'logout/$',logout, name="logout"),
    url(r'subrecord/$', subrecord, name="subrecord"),
    url(r'to_change_passwd/$', tochangePasswd, name="to_change_passwd"),
    url(r'change_passwd/$', changepasswd, name="change_passwd"),
]
