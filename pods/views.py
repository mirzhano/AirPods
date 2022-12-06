from django.shortcuts import render
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
