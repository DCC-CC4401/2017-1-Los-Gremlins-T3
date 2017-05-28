from django.conf.urls import url

from . import views

app_name = 'ficha_vendedor'

urlpatterns = [
    url(r'(\d*)', views.fichavendedor, name='vendedor-profile-page'),
    #url(r'^$', views.profile, name='profile'),

]