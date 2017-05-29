
from django import forms
from user.models import AbstractUser, PaymentMethod

from django.contrib.auth.forms import UserCreationForm
from django.conf import settings


class StudentEditForm(forms.Form):
    email = forms.EmailField(label='E-Mail',
                             max_length=254,
                             required=False)

    # TODO: Avatar change

    password = forms.CharField(label='Nueva Contraseña',
                               widget=forms.PasswordInput,
                               required=False)
    password2 = forms.CharField(label='Repite nueva contraseña',
                                widget=forms.PasswordInput,
                                required=False)

    def pass_is_valid(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            password2 = self.cleaned_data['password2']
            if password == password2:
                return True
        return False

class SignUpForm(forms.Form):
    # Common data (Student & Sellers)
    email = forms.EmailField(label='E-Mail',
                             max_length=254,
                             help_text='Requerido. Se utiliza para ingresar al sistema')
    account_type = forms.ChoiceField(label='Tipo de cuenta',
                                     choices=[(1, "Alumno"), (2, "Vendedor Ambulante"), (3, "Vendedor Fijo")],
                                     help_text='Selecciona uno.')
    fullname = forms.CharField(label='Nombre completo',
                               max_length=128,
                               help_text='Requerido. Tu nombre o el nombre de tu tienda.')
    password = forms.CharField(label='Contraseña',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite contraseña',
                                widget=forms.PasswordInput)
    # Hide fields with jquery depending of accoutn
    # Fixed Seller no Walkin Seller & Student
    start_hour = forms.TimeField(label='Horario de apertura',
                                 widget=forms.TimeInput(),
                                 initial='10:00')
    end_hour = forms.TimeField(label='Horario de cierre',
                               widget=forms.TimeInput(),
                               initial='10:00')
    address = forms.CharField(label="Dirección del local",
                              max_length=128)

    # Walking Seller & Fixed Seller no Student
    pay_methods = forms.ModelMultipleChoiceField(label='Metodos de pago',
                                                 queryset=PaymentMethod.objects.all())

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




