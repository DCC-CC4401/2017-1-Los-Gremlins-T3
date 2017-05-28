from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.conf import settings
from producto.models import Producto

_labels = [
    r'<label class="prev" "for="test1"><imgsrc="/static/app/img/bread.png',
    r'<label class="prev" "for="test2"><imgsrc="/static/app/img/bread.png',
    r'<label class="prev" "for="test3"><imgsrc="/static/app/img/bread.png',
    r'<label class="prev" "for="test4"><imgsrc="/static/app/img/bread.png',
    r'<label class="prev" "for="test5"><imgsrc="/static/app/img/bread.png',
    r'<label class="prev" "for="test6"><imgsrc="/static/app/img/bread.png',
    r'<label class="prev" "for="test7"><imgsrc="/static/app/img/bread.png',
    r'<label class="prev" "for="test8"><imgsrc="/static/app/img/bread.png',
    r'<label class="prev" "for="test9"><imgsrc="/static/app/img/bread.png',
    r'<label class="prev" "for="test10"><imgsrc="/static/app/img/bread.png',
    r'<label class="prev" "for="test11"><imgsrc="/static/app/img/bread.png',
    r'<label class="prev" "for="test12"><imgsrc="/static/app/img/bread.png',
    r'<label class="prev" "for="test13"><imgsrc="/static/app/img/bread.png',
    r'<label class="prev" "for="test14"><imgsrc="/static/app/img/bread.png',
    r'<label class="prev" "for="test15"><imgsrc="/static/app/img/bread.png',
    r'<label class="prev" "for="test16"><imgsrc="/static/app/img/bread.png',
    r'<label class="prev" "for="test17"><imgsrc="/static/app/img/bread.png',
    r'<label class="prev" "for="test18"><imgsrc="/static/app/img/bread.png',
    r'<label class="prev" "for="test19"><imgsrc="/static/app/img/bread.png',
]

_choices = [(id, mark_safe(_(_labels[id]))) for id in range(len(_labels))]

class CreateProductoForm(forms.Form):
    name = forms.CharField(label='Nombre del producto', max_length=128)
    price = forms.IntegerField(label='Precio del Producto')
    stock = forms.IntegerField(label='Stock del producto')
    description = forms.CharField(label='Descripción', widget=forms.Textarea)
    prev_img = forms.ChoiceField(label='Seleccione una imagen previa',
                                 widget=forms.RadioSelect,
                                 choices=_choices)
    img = forms.FileField(label='Imagen del producto')
