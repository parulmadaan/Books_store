from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Books


class createbookform(forms.Form):
    author = forms.CharField(max_length=100)
    title = forms.CharField(max_length=100)
    Price = forms.IntegerField()
    Edition = forms.IntegerField()

    class Meta:
        model=Books
        fields=('author','title','Price','Edition')
