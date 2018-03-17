from django.conf.urls import url
from movie.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'page/(?P<num>[1-9]+[0-9]*)$', getPage, name="getPage"),
    url(r'detial/(?P<id>[^0][0-9]*)$', detail, name="detail"),
    url(r'search/$', search, name="search")
]