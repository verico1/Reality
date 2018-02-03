from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^account/register/$', views.register, name='register'),
    url(r'^account/login/$', views.login, name='login'),
    url(r'^account/logout/$', views.logoutt, name='logout'),
    url(r'^account/$', views.account, name='account'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^call_us/$', views.call_us, name='call_us')
]
