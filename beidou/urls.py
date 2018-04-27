from django.conf.urls import url
from beidou.views import *
from django.views.generic.base import TemplateView
urlpatterns = [
    url(r'^$', index),
    url(r'contact/$', contact),
    url(r'memberinfo/$', memberinfo),
    url(r'toregister/$', TemplateView.as_view(template_name="beidou/register.html"), name="toregister"),
    url(r'register/$', register, name="register"),
    url(r'login/$', login, name="login"),
    url(r'logout/$', logout, name="logout"),
    url(r'toaddmember/$', toaddmember, name="toaddmember"),
    url(r'addmember/$', addmember, name="addmember"),
    url(r'memberdetail/\d+/$', memberdetail, name="memberdetail"),
    url(r'getdata/$', getdata, name="getdata"),
]