from django.shortcuts import render
from .models import header
# Create your views here.
def index(request) :
    headers = header.objects.all()
    return  render(request , "home.html" , {'headers' : headers})
