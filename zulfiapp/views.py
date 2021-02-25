from django.shortcuts import render
from .models import header
# Create your views here.
def index(request) :
    headers = header.objects.filter()
    print(headers[0].image)
    header1 = header.objects.all().first()
    return  render(request , "home.html" , {'headers' : headers , 'header1' :header1})
