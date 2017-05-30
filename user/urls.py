from django.conf.urls import url

from . import views

app_name = 'user'

urlpatterns = [
    url(r'^signup/', views.signup, name='signup'),
    url(r'^admin_signup', views.admin_signup, name='admin_signup'),
    url(r'(\d*)/edit', views.edit_student, name='edit_student'),
    url(r'(\d*)/delete', views.delete_student, name='delete_student')
    #url(r'^$', views.profile, name='profile'),

]
