from django.conf.urls import url

from . import views

app_name = 'ficha_vendedor'

urlpatterns = [
    url(r'(\d*)/edit', views.seller_edit, name='edit'),
    #url(r'^$', views.profile, name='profile'),

]