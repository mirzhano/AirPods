from django.shortcuts import render, get_object_or_404
from django.views import generic

from . import models, forms


def main_page(request):
   info = models.Order.objects.all()
   print(info)
   return render(request, "order.html", {"info": info})


def home(request):
   head = models.Home.objects.all()
   return render(request, 'order.html', {'head': head})


def show_details(request, id):
   seria = get_object_or_404(models.Order, id=id)
   return render(request, 'order.html', {'seria': seria})


class Create(generic.CreateView):
   template_name = 'add.html'
   form_class = forms.AddForm
   queryset = models.Order.objects.all()
   success_url = '/order/'

   def form_valid(self, form):
      print(form.cleaned_data)
      return super(Create, self).form_valid(form=form)


class Update(generic.UpdateView):
   template_name = 'update.html'
   form_class = forms.AddForm
   success_url = '/order/'

   def get_object(self, **kwargs):
      note_id = self.kwargs.get('id')
      return get_object_or_404(models.Order, id=note_id)

   def form_valid(self, form):
      return super(Update, self).form_valid(form=form)



class Delete(generic.DeleteView):
   template_name = 'delete.html'
   success_url = '/order/'

   def get_object(self, **kwargs):
      _id = self.kwargs.get('id')
      return get_object_or_404(models.Order, id=_id)


