from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100,  help_text='Required. Inform a valid email address.')
    password = forms.CharField(max_length =100)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'avatar')


class LogInForm(forms.Form):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('email','password' )

class sendemailForm(forms.Form):
    email = forms.EmailField()

    def __str__(self):
        return self.email
