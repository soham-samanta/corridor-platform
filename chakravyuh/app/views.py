from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(req):
#     return HttpResponse("Hello Peeps !! Corridoor") 

def index1(req):
    return render(req,'index.html')

def handle_file_upload(request):
    if request.method == 'POST' and 'csv-file' in request.FILES:
        csv_file = request.FILES['csv-file']
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
