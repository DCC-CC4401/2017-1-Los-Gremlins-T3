
from django import forms
from user.models import AbstractUser

from django.contrib.auth.forms import UserCreationForm
from django.conf import settings


class RegistroVendedorFijoForm(forms.Form):
    fullname = forms.CharField(label='Full name', max_length=100)


class SignUpForm(forms.Form):
    email = forms.EmailField(max_length=254, label='E-Mail', help_text='Requerido. Se utiliza para ingresar al sistema')
    account_type = forms.ChoiceField(label='Tipo de cuenta', choices=[(1, "Alumno"), (2, "Vendedor Ambulante"), (3, "Vendedor Fijo")], help_text='Selecciona uno.')
    fullname = forms.CharField(label='Nombre completo', max_length=128, help_text='Requerido. Tu nombre o el nombre de tu tienda.')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite contraseña', widget=forms.PasswordInput)

    class Meta:
        model = AbstractUser
        fields = ('fullname', )

    def pass_is_valid(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            password2 = self.cleaned_data['password2']
            if password == password2:
                return True
        return False




