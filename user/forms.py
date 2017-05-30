
from django import forms
from user.models import AbstractUser, PaymentMethod
from django.utils.safestring import mark_safe

from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
_alabels = [
    '<label class="prev" "for="test1"><img src="/static/app/img/AvatarEstudiante1.png"/>\
    </label>',
    '<label class="prev" "for="test2"><img src="/static/app/img/AvatarEstudiante2.png"/>\
    </label>',
    '<label class="prev" "for="test3"><img src="/static/app/img/AvatarEstudiante3.png"/>\
    </label>',
    '<label class="prev" "for="test4"><img src="/static/app/img/AvatarEstudiante4.png"/>\
    </label>',
]
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

_achoices = [(id, mark_safe(_alabels[id])) for id in range(len(_alabels))]

_schoices = [(id, mark_safe(_slabels[id])) for id in range(len(_slabels))]
_radio_attrs = {
    'class': 'with-gap',
    'name': 'group1',
    'id': 'test1'
}

class StudentEditForm(forms.Form):
    email = forms.EmailField(label='E-Mail',
                             max_length=254,
                             required=False)

    fullname = forms.CharField(label='Nombre completo',
                               max_length=128,
                               required=False)

    student_avatar = forms.ChoiceField(label='Alumno, selecciona una avatar',
                                    widget=forms.RadioSelect,
                                    choices=_achoices)


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

    student_avatar = forms.ChoiceField(label='Alumno, selecciona un avatar',
                                    widget=forms.RadioSelect,
                                    choices=_achoices,
                                       initial=0)

    seller_avatar = forms.ChoiceField(label='Vendedor, selecciona un avatar',
                                    widget=forms.RadioSelect,
                                    choices=_schoices,
                                      initial=1)

    password = forms.CharField(label='Contraseña',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite contraseña',
                                widget=forms.PasswordInput)
    # Hide fields with jquery depending of accoutn
    # Fixed Seller no Walkin Seller & Student
    start_hour = forms.TimeField(label='Horario de apertura',
                                 widget=forms.TimeInput(format='%H:%M'),
                                 initial='10:00')
    end_hour = forms.TimeField(label='Horario de cierre',
                               widget=forms.TimeInput(format='%H:%M'),
                               initial='20:00')
    address = forms.CharField(label="Dirección del local",
                              max_length=128)

    # Walking Seller & Fixed Seller no Student
    pay_methods = forms.ModelMultipleChoiceField(label='Metodos de pago',
                                                 queryset=PaymentMethod.objects.all(),
                                                 required=True)

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


class AdminSignUpForm(forms.Form):
    # Common data (Student & Sellers)
    email = forms.EmailField(label='E-Mail',
                             max_length=254,
                             help_text='Requerido. Se utiliza para ingresar al sistema')
    fullname = forms.CharField(label='Nombre completo',
                               max_length=128,
                               help_text='Requerido. Tu nombre o el nombre de tu tienda.')
    password = forms.CharField(label='Contraseña',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite contraseña',
                                widget=forms.PasswordInput)
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



