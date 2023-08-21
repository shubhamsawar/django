from django.shortcuts import render,HttpResponseRedirect
from django.conf import settings
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import requests
from dateutil import parser
from . models import news





# Create your views here.
@login_required
def home(request):
    url = "https://newsapi.org/v2/everything?q=tesla&from=2023-07-21&sortBy=publishedAt&apiKey="+ str(settings.API_KEY)
    print(url)
    res = requests.get(url=url).json()['articles']
    for i in range(len(res)):
        au = res[i]['author']
        tt = res[i]['title']
        ds = res[i]['description'[:12]]
        dt = parser.parse(res[i]['publishedAt'])
        ur = res[i]['url']
        im =res[i]['urlToImage']
        news.objects.get_or_create(author=au,title=tt,desc=ds,date=dt,urls=ur,img=im)
    my_list = news.objects.all().order_by('-date').distinct()
    return render(request,'core/home.html',{'news':my_list})


def search(request):
    if request.method == 'GET':
        value = request.GET.get('q',None)
        valu2 = request.GET.get('search')
        if value is not None:
            qs = news.objects.filter(Q(title__icontains=value)|Q(author__icontains=value))
        else:
            qs={}
    return render(request,'core/search.html',{'data': qs.order_by('-date')})


        


