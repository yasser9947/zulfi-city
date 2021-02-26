from django.shortcuts import render
from .models import header, AboutUs , News
# Create your views here.


def index(request) :
    headers = header.objects.filter()
    print(headers[0].image)
    aboutUs = AboutUs.objects.filter()
    order = ['first' , 'second' , 'third' , 'fourth']
    i=0
    for x in aboutUs:
        x.avatar = order[i]
        print(x.avatar)
        i = i + 1 
    
    header1 = header.objects.all().first()

    news = News.objects.filter()
    return  render(request , "home.html" , {
        'headers' : headers , 
        'header1' :header1, 
        'aboutUs' :aboutUs,
        'order'   : order  ,
        "news" : news      
        })
