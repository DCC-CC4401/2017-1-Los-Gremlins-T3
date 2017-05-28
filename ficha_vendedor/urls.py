from django.conf.urls import url

from . import views

app_name = 'fichavendedor'

urlpatterns = [
    url(r'^', views.fichavendedor(), name='vendedor-profile-page'),
    #url(r'^$', views.profile, name='profile'),

]