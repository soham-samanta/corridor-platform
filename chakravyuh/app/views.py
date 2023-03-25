import os
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from extract.graphs import exctocsvtopandas, confmat
from toword.docxgen import doccreate
# Create your views here.

# def index(req):
#     return HttpResponse("Hello Peeps !! Corridoor") 

def index1(req):
    return render(req,'index.html')

def handle_file_upload(request):
    if request.method == 'POST' and 'csv-file' in request.FILES:
        csv_file = request.FILES['csv-file']
        x_value = request.POST['x-value']
        y_value = request.POST['y-value']
        t_value = request.POST['t-value']
        data_dir = os.path.join(settings.BASE_DIR, 'data')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        with open(os.path.join(data_dir, csv_file.name), 'wb') as f:
            for chunk in csv_file.chunks():
                f.write(chunk)
        
        with open(os.path.join(data_dir, 'values.txt'), 'w') as f2:
            f2.write(x_value + '\n')
            f2.write(y_value + '\n')
            f2.write(t_value + '\n')
        df = exctocsvtopandas()
        print(df)
        print(type(df))
        confmat(x_value, y_value, t_value, df)
        doccreate()
            
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
