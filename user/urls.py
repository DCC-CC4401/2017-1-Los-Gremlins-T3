from django.conf.urls import url

from . import views

app_name = 'user'

urlpatterns = [
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/submit', views.loginResponse, name='loginResponse'),
    #url(r'^$', views.profile, name='profile'),

]
