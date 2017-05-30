

from django import forms
from user.models import AbstractUser, PaymentMethod

from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.utils.safestring import mark_safe


class RegistroVendedorFijoForm(forms.Form):
    fullname = forms.CharField(label='Full name', max_length=100)

_slabels = [
    '<label class="prev" "for="test1"><img src="/static/app/img/AvatarVendedor1.png"/>\
    </label>',
    '<label class="prev" "for="test2"><img src="/static/app/img/AvatarVendedor2.png"/>\
    </label>',
    '<label class="prev" "for="test3"><img src="/static/app/img/AvatarVendedor3.png"/>\
    </label>',
    '<label class="prev" "for="test4"><img src="/static/app/img/AvatarVendedor4.png"/>\
    </label>',
    '<label class="prev" "for="test4"><img src="/static/app/img/AvatarVendedor5.png"/>\
    </label>',
    '<label class="prev" "for="test4"><img src="/static/app/img/AvatarVendedor6.png"/>\
    </label>',
]

_schoices = [(id, mark_safe(_slabels[id])) for id in range(len(_slabels))]
_radio_attrs = {
    'class': 'with-gap',
    'name': 'group1',
    'id': 'test1'
}


class FixedSellerEditForm(forms.Form):
    email = forms.EmailField(label='E-Mail',
                             widget=forms.EmailInput(attrs={'id':'mail'}),
                             max_length=254,
                             required=False)

    fullname = forms.CharField(label='Nombre de tienda',
                               widget=forms.TextInput(attrs={'id':'fullname'}),
                               max_length=128,
                               required=False)

    seller_avatar = forms.ChoiceField(label='Vendedor, selecciona un avatar',
                                    widget=forms.RadioSelect(attrs={'id':'avatar'}),
                                    choices=_schoices,
                                      required=False)

    pay_methods = forms.ModelMultipleChoiceField(label='Metodos de pago',
                                                 queryset=PaymentMethod.objects.all(),
                                                 required=False)

    start_hour = forms.TimeField(label='Horario de apertura',
                                 widget=forms.TimeInput(),
                                 required=False)
    end_hour = forms.TimeField(label='Horario de cierre',
                               widget=forms.TimeInput(),
                               required=False)
    address = forms.CharField(label="Dirección del local",
                              max_length=128,
                              required=False)

    password = forms.CharField(label='Nueva Contraseña',
                               widget=forms.PasswordInput,
                               required=False)
    password2 = forms.CharField(label='Repite nureva contraseña',
                                widget=forms.PasswordInput,
                                required=False)

    def pass_is_valid(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            password2 = self.cleaned_data['password2']
            if password == password2:
                return True
        return False



class WalkingSellerEditForm(forms.Form):
    email = forms.EmailField(label='E-Mail',
                             max_length=254,
                             required=False)

    fullname = forms.CharField(label='Nombre de tienda',
                               max_length=128,
                               required=False)

    seller_avatar = forms.ChoiceField(label='Vendedor, selecciona un avatar',
                                    widget=forms.RadioSelect,
                                    choices=_schoices,
                                      required=False)

    pay_methods = forms.ModelMultipleChoiceField(label='Metodos de pago',
                                                 queryset=PaymentMethod.objects.all(),
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




