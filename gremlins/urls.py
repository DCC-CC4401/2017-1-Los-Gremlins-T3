"""gremlins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from homepage import views as home_views
from ficha_vendedor import views as ficha_vendedor_views

from . import views
from user import views as userViews

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'gestionproductos', views.gestionproductos, name='gestionproductos'),

    # Ficha_vendedor
    url(r'ficha_vendedor/(\d*)$', ficha_vendedor_views.fichavendedor, name='ficha_vendedor'),


    # Homepage
    url(r'^$', home_views.index, name='index'),

    # User
    url(r'^user/login/$', auth_views.login, {'template_name':'user/login.html'}, name='login'),
    url(r'^user/logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'user/', include('user.urls', namespace='user')),
]
