
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings


class RegistroVendedorFijoForm(forms.Form):
    fullname = forms.CharField(label='Full name', max_length=100)

class SignUpForm(forms.Form):
    fullname = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254, help_text='Requerido. Se usa como usuario para ingresar al sistema.')
    passwd = forms.CharField(widget=forms.PasswordInput)





