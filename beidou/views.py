from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
import datetime
import json

from beidou.models import *
from movie.models import *
# Create your views here.

def index(request):
    response = render(request, "beidou/temperature.html")
    t = Items.objects.order_by('-id')[:5]
    response.set_cookie('id', t[4].id)
    return response

# def index(request):
#     return render(request, "beidou/index.html")

@login_required  
def contact(request):
    member = Member.objects.filter(supervisor=request.user)

    return render(request, "beidou/contact.html", {'member':member})

@login_required  
def memberinfo(request):
    return render(request, "beidou/ConcreteIndex.html")

def register(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    email = request.POST.get('email','')
    user = auth.authenticate(username=username, password=password)
    if user:
        return HttpResponse("用户已经存在！")
    user = User.objects.create_user(username=username, email=email, password=password) # 添加到数据库（还可以加一些字段的处理）
    user.save()
    #添加到session
    request.session['username'] = username
    #调用auth登录
    login(request, user)
    #重定向到首页
    return redirect('/')

def login(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    print(password,username)
    user = auth.authenticate(username=username, password=password)
    if not user is None:
        auth.login(request, user)
        return redirect('/')
    else:
        return HttpResponse("用户名或密码错误！请检查后再尝试登陆。")

def logout(request):
    auth.logout(request)
    return redirect('/')
    
@login_required 
def toaddmember(request):
    return render(request, "beidou/addmember.html")

@login_required 
def addmember(request):
    name = request.POST.get('name',None)
    birthdate = request.POST.get('birthdate',None)
    gender = request.POST.get('gender',None)
    height = request.POST.get('height',None)
    weight = request.POST.get('weight',None)
    height = float(height)
    weight = float(weight)
    birthdate = datetime.datetime.strptime(birthdate,"%Y-%m-%d").date()
    try:
        Member.objects.create(
            supervisor=request.user,
            name=name,
            gender=gender,
            birthdate=birthdate,
            height=height,
            weight=weight,                 
        )
        return HttpResponse("1")
    except:
        return HttpResponse("0")


def memberdetail(request):
    return render(request, "beidou/ConcreteIndex.html")

def getdata(request):
    id = request.COOKIES["id"]
    d = Items.objects.filter(id=id).values_list('name', 'img')[0]
    d = list(d)
    response = HttpResponse(json.dumps(d), content_type="application/json")
    response.set_cookie('id', int(id)+1)
    return HttpResponse(json.dumps(d), content_type="application/json")



