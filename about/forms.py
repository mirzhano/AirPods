


from django import forms
from .models import Comment





class AddForm(forms.ModelForm):

      class Meta:
         model = Comment
         fields = ('__all__')