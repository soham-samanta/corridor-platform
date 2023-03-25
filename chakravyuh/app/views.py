from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(req):
#     return HttpResponse("Hello Peeps !! Corridoor") 

def index1(req):
    return render(req,'index.html')