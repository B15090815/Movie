from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
import os
from collect.models import Experiment,Exptemplate
from django.contrib.auth.decorators import login_required 
from django.conf import settings
from datetime import datetime
# Create your views here.

def index(request):
    if request.user.is_authenticated():
        exptemplate = Exptemplate.objects.filter(isactive=True)
        exp = Experiment.objects.filter(user=request.user)
        return render(request,'collect/index.html', {'exp':exp, 'exptemplate':exptemplate})
    else:
        return render(request,'collect/index.html')

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

def subrecord(request):
    exp = request.POST.get('exp', '')
    if exp != '':
        record = request.FILES.get("record", None)
        if record != None:
            fileSuffix = record.name.split('.')[-1]
            idnum = request.user.username
            nametemlate = Exptemplate.objects.get(name=exp).nameformate
            filename = nametemlate.format(exp=exp,idnum=idnum,name=request.user.first_name,fileSuffix=fileSuffix)

            #temlate = "{exp}_{idnum}_{name}.{fileSuffix}".format(exp="实验一",idnum="B15090815",name="陈仁祥",fileSuffix="doc")
            dirName = os.path.join(settings.MEDIA_ROOT , "B150403", exp)

            try:
                if not os.path.exists(dirName):
                    os.makedirs(dirName)

                filePath = os.path.join(dirName,filename)
                open(filePath,'wb').write(record.file.read())
                experiment = Experiment.objects.filter(expname=filename)
                if experiment.exists():
                    experiment.update(submitdate=datetime.now())
                else:
                    Experiment.objects.create(user=request.user, expname=filename, filepath=filePath, submitdate=datetime.now())
                return HttpResponse("1")
            except Exception as e:
                print(str(e))
                return HttpResponse("2")
    else:
        return HttpResponse("0")


@login_required
def changepasswd(request):
    old_passwd  = request.POST.get('old_passwd','')
    new_passwd = request.POST.get('new_passwd', '')
    user = auth.authenticate(username=request.user.username, password=old_passwd)
    if user is not None and user.is_active:
        user.set_password(new_passwd)
        user.save()
        auth.logout(request)
        return render(request,'collect/index.html', {'change_passwd':True})
    else:
        return render(request,"collect/changepasswd.html",{'fail':True})

@login_required
def tochangePasswd(request):
    return render(request,"collect/changepasswd.html")
