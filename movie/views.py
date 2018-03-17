import math
import json
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from movie.models import Items, Links
# Create your views here.

# select *
# from movie_items order
#
# by
# id
# desc
# limit
# 2, 4;
def test(request):
    return render_to_response('movie/detail.html')


def index(request):
    # response.set_cookie('<cookie_name>', value)
    # if request.COOKIES.get('pageNum', None):
    #     pageNum = request.COOKIES.get('pageNum')
    # else:
    #     pageNum = 1
    movieNum = Items.objects.count()
    endPage = math.ceil(movieNum / 20)
    movieList = Items.objects.all().order_by("-id")[:20]
    response = render(request, 'movie/index.html', {"MovieList": movieList})
    response.set_cookie('pageNum', 1)
    response.set_cookie('endPage', endPage)
    return response

def getPage(request,num):
    start = int(num)
    start = (start-1) * 20
    movieNum = Items.objects.count()
    end = start + 20
    if end > movieNum:
        end = movieNum
    movieObject = Items.objects.order_by("-id").all().values()[start:end]
    movieList = list(movieObject)
    response = HttpResponse(
        json.dumps(movieList), content_type="application/json")
    response.set_cookie('pageNum', num)
    return response

def detail(request,id):
    try:
        item = Items.objects.values('name', 'img', 'tag', 'pubdate').get(id=id)
        if item['tag'] == "":
            link = Links.objects.values_list(
                'link', flat=True).order_by('-link').filter(item_id=id)
        else:
            link = Links.objects.values_list(
                'link', flat=True).filter(item_id=id)
    except Exception as e:
        print(str(e))
        item = []
        link = []
    return render(request, 'movie/detail.html', {"item": item, "link": link})

def search(request):
    key = request.GET.get("key",None)
    if key != None:
        movieList = Items.objects.filter(name__contains=key)
        response = render(request, 'movie/result.html', {
            "MovieList": movieList
        })
    else:
        response = render(request, 'movie/index.html', {
            "Nokey": 1
        })
    return response

