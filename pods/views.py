from django.shortcuts import render, get_object_or_404
from . import models


# Create your views here.

def header(request):
    headers = models.Pods.objects.all()
    pic = models.Pic.objects.all()
    post = models.Post.objects.all()

    context = {
        'headers': headers,
        'pic': pic,
        'post': post,

    }
    return render(request, 'index.html', context)


def show_all(request):
    air = models.Cat.objects.all()
    return render(request, 'index.html', {'air': air})


def show_details(request, id):
    airpod = get_object_or_404(models.Cat, id=id)
    return render(request, 'details.html', {'airpod': airpod})

# def reg(request):
#     return render(request, 'login.html')
