from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.conf import settings
from producto.models import Producto

_labels = [
    '<label class="prev" "for="test1"><img src="/static/app/img/bread.png"/>\
    </label>',
    '<label class="prev" "for="test2"><img src="/static/app/img/breakfast.png"/>\
    </label>',
    '<label class="prev" "for="test3"><img src="/static/app/img/burger.png"/>\
    </label>',
    '<label class="prev" "for="test4"><img src="/static/app/img/chicken.png"/>\
    </label>',
    '<label class="prev" "for="test5"><img src="/static/app/img/chicken2.png"/>\
    </label>',
    '<label class="prev" "for="test6"><img src="/static/app/img/chocolate.png"/>\
    </label>',
    '<label class="prev" "for="test7"><img src="/static/app/img/coke.png"/>\
    </label>',
    '<label class="prev" "for="test8"><img src="/static/app/img/cupcake.png"/>\
    </label>',
    '<label class="prev" "for="test9"><img src="/static/app/img/donut.png"/>\
    </label>',
    '<label class="prev" "for="test10"><img src="/static/app/img/jelly.png"/>\
    </label>',
    '<label class="prev" "for="test11"><img src="/static/app/img/fish.png"/>\
    </label>',
    '<label class="prev" "for="test12"><img src="/static/app/img/fries.png"/>\
    </label>',
    '<label class="prev" "for="test13"><img src="/static/app/img/hot-dog.png"/>\
    </label>',
    '<label class="prev" "for="test14"><img src="/static/app/img/icecream.png"/>\
    </label>',
    '<label class="prev" "for="test15"><img src="/static/app/img/juice.png"/>\
    </label>',
    '<label class="prev" "for="test16"><img src="/static/app/img/lettuce.png"/>\
    </label>',
    '<label class="prev" "for="test17"><img src="/static/app/img/pizza.png"/>\
    </label>',
    '<label class="prev" "for="test18"><img src="/static/app/img/spaguetti.png"/>\
    </label>',
    '<label class="prev" "for="test19"><img src="/static/app/img/rice.png"/>\
    </label>',
]

_choices = [(id, mark_safe(_(_labels[id]))) for id in range(len(_labels))]

_attributes = {
    'name': {
        'class': 'validate',
        'name': 'item',
        'id': 'item'
    },
    'price': {
        'class': 'validate',
        'name': 'precio',
        'id': 'precio'
    },
    'stock': {
        'class': 'validate',
        'name': 'stock',
        'id': 'stock'
    },
    'desc': {
        'class': 'materialize-textarea',
        'id': 'icon_prefix2'
    },
}

_radio_attrs = {
    'class': 'with-gap',
    'name': 'group1',
    'id': 'test1'
}

class CreateProductoForm(forms.Form):
    name = forms.CharField(label='Nombre del producto',
                           max_length=128,
                           widget=forms.TextInput(attrs=_attributes['name']))

    price = forms.IntegerField(label='Precio del Producto',
                               widget=forms.NumberInput(
                                   attrs=_attributes['price']))

    stock = forms.IntegerField(label='Stock del producto',
                               widget=forms.NumberInput(
                                   attrs=_attributes['stock']))

    description = forms.CharField(label='Descripción',
                                  widget=forms.Textarea(
                                      attrs=_attributes['desc']))

    prev_img = forms.ChoiceField(label='Selecciona una imagen previa',
                                 widget=forms.RadioSelect(
                                     attrs=_radio_attrs),
                                 choices=_choices)
    img = forms.FileField(label='Imagen del producto')

    class Meta:
        model = Producto
