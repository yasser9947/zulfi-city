from django.shortcuts import render
from .models import header, AboutUs , News ,OurPortfolio
# Create your views here.


def index(request) :
    headers = header.objects.filter()
    aboutUs = AboutUs.objects.filter()
    order = ['first' , 'second' , 'third' , 'fourth']
    i=0
    for x in aboutUs:
        x.avatar = order[i]
        i = i + 1 
    
    header1 = header.objects.all().first()
    ourPortfolio = OurPortfolio.objects.filter()
    # print(ourPortfolio[0].image.all())
    news = News.objects.filter()
    return  render(request , "home.html" , {
        'headers' : headers , 
        'header1' :header1, 
        'aboutUs' :aboutUs,
        'order'   : order  ,
        "news" : news  ,  
        'ourPortfolio': ourPortfolio   
        })
