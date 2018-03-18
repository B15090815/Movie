from django.shortcuts import render, HttpResponse
from vip.models import *
import json
import requests
from bs4 import BeautifulSoup
import re
import hashlib

# Create your views here.


def index(request):
    return render(request, 'vip/index.html')


def searcher(request):
    name = request.POST.get('q', '')
    link = Links.objects.select_related().filter(item__name__contains=name).values_list()
    url = 'http://www.soku.com/search_video/q_' + name
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'
    headers = {'User-Agent': user_agent}
    try:
        r = requests.get(url, headers=headers)
    except Exception:
        return HttpResponse(json.dumps({'tv': [], 'movie': []}), content_type="application/json")
    soup = BeautifulSoup(r.text, 'html.parser')
    tv_items = soup.find_all('div', class_='s_tv clearfix')
    mv_items = soup.find_all('div', class_='s_movie clearfix')

    tv_source = []
    for each in tv_items:
        img = 'http:' + each.find('img').get('src')
        title = each.find('h2', class_='base_name').find('a').get('_log_title')
        temp = each.find('div', class_=re.compile(r'^s_items all'))
        if not bool(temp):
            temp = each.find('div', class_=re.compile(r'^s_items'))
            if temp:
                links = [one['href'] for one in temp.find_all('a')]
            else:
                links = []
        else:
            links = [one['href'] for one in temp.find_all('a')]
            links.pop()

        tv_source.append({'title': title, 'img': img, 'links': links})

    mv_source = []
    for each in mv_items:
        img = 'http:' + each.find('img').get('src')
        title = each.find('h2', class_='base_name').find('a').get('_log_title')
        link = []
        temp = each.find('a', class_='btn_play')
        if temp:
            link.append(temp.get('href', 'none'))
        else:
            link.append('#')
        mv_source.append({'title': title, 'img': img, 'links': link})

        for tv in tv_source:
            item = Items.objects.create(name=tv['title'], img=tv['img'])
            Links.objects.create(item=item, link=str(tv['links']))

        for mv in mv_source:
            item = Items.objects.create(name=mv['title'], img=mv['img'])
            Links.objects.create(item=item, link=str(mv['links']))

    return HttpResponse(json.dumps({'tv': tv_source, 'movie': mv_source}), content_type="application/json")


def parse(request):
    if request.method == "GET":
        url = request.GET.get('url')
    return render(request, 'vip/parse.html',{'url':url})

# def addparse(request):
#     url = request.GET.get()
