from django.conf.urls import url

from . import views

app_name = 'user'

urlpatterns = [
    url(r'^signup/', views.signup, name='signup'),
    #url(r'^$', views.profile, name='profile'),

]
