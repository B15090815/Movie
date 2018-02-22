from django.conf.urls import url
from vip.views import *
urlpatterns = [
    url(r'^$', index),
]