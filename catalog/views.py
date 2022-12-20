from django.shortcuts import render, get_object_or_404
from . import models

def main_page(request):
    info = models.Cat.objects.all()
    print(info)
    return render(request, "catalog.html", {"info": info})

def main(request):
    info = models.Cat.objects.all()
    print(info)
    return render(request, "catalog.html", {"info": info})

def home(request):
    head = models.Home.objects.all()
    return render(request, 'catalog.html', {'head': head})

def show_all(request):
    air = models.Cat.objects.all()
    return render(request, 'catalog.html', {'air': air})

def show_details(request, id):
    airpod = get_object_or_404(models.Cat, id=id)
    return render(request, 'details.html', {'airpod': airpod})


def about_us(request):
    about_us = models.About_us.objects.all()
    return render(request, 'about_us.html', {'about_us': about_us})