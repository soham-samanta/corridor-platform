import os
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
# Create your views here.

# def index(req):
#     return HttpResponse("Hello Peeps !! Corridoor") 

def index1(req):
    return render(req,'index.html')

def handle_file_upload(request):
    if request.method == 'POST' and 'csv-file' in request.FILES:
        csv_file = request.FILES['csv-file']
        data_dir = os.path.join(settings.BASE_DIR, 'data')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        with open(os.path.join(data_dir, csv_file.name), 'wb') as f:
            for chunk in csv_file.chunks():
                f.write(chunk)
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
