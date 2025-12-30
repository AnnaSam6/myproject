import os
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, 'app/home.html')

def current_time_view(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Текущее время: {current_time}")

def workdir_view(request):
    files = os.listdir()
    files_list = "<br>".join(files)
    return HttpResponse(f"Содержимое рабочей директории:<br>{files_list}")
