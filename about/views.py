from django.shortcuts import render, get_object_or_404
from django.views import generic

from . import models, forms
from django.urls import reverse_lazy
from django.views.generic import CreateView
# from .forms import CommentForm


# Create your views here.
def about(request):
    about = models.About.objects.all()
    second = models.Second.objects.all()

    context = {
        'about': about,
        'second': second,

    }
    return render(request, 'about_us.html', context)


def about(request):
   info = models.Comment.objects.all()
   print(info)
   return render(request, "about_us.html", {"info": info})


class Create(generic.CreateView):
   template_name = 'about.html'
   form_class = forms.AddForm
   queryset = models.Comment.objects.all()
   success_url = '/about_us/'

   def form_valid(self, form):
      print(form.cleaned_data)
      return super(Create, self).form_valid(form=form)


class Update(generic.UpdateView):
   template_name = 'update.html'
   form_class = forms.AddForm
   success_url = '/about_us/'

   def get_object(self, **kwargs):
      note_id = self.kwargs.get('id')
      return get_object_or_404(models.Comment, id=note_id)

   def form_valid(self, form):
      return super(Update, self).form_valid(form=form)



class Delete(generic.DeleteView):
   template_name = 'delete.html'
   success_url = '/about_us/'

   def get_object(self, **kwargs):
      _id = self.kwargs.get('id')
      return get_object_or_404(models.Comment, id=_id)



# def create(request):
#     form: CommentForm
#     data = {
#         'form': form
#     }
#
#     return render(request, 'about_us.html', data)
# class SignUpView(CreateView):
#     form_class = CommentForm
#     success_url = reverse_lazy('/')
#     template_name = "about_us.html"