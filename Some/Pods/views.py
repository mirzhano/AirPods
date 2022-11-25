from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView
from . import models

from django.views import generic
#олучение информации (get)

# class home(TemplateView):  # просмотр начальной страницы
#     model = models.Pods
#     template_name = "index.html"
def main_page(request):
    info = models.Pods.objects.all()
    print(info)
    return render(request, "index.html", {"info": info})

def home(request):
    head = models.Home.objects.all()
    return render(request, 'index.html', {'head': head})

def show_all(request):
    air=models.Pods.objects.all()
    return render(request,'index.html', {'air':air})

def characteristic(request):
    character=models.Characteristic.objects.all()
    return render(request, 'characteristic.html',{'character': character})

def about_us(request):
    about_us=models.About_us.objects.all()
    return render(request, 'about_us.html',{'about_us': about_us})

# def home(request):
#     return render(request, 'index.html')
#
#
# def air3(request):
#     return render(request, "airpods-3.html")
#
# def airmax(request):
#     return render(request,"airpods-max.html")
#
# def airpro(request):
#     return render( request,"airpods-pro.html")

def show_details(request, id):
    airpod = get_object_or_404(models.Pods, id=id)
    return render(request, 'details.html', {'airpod': airpod})


