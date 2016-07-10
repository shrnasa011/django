from django.conf.urls import url, include
#from django.conf.urls.defaults import *
from django.contrib import admin
from login import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.login, name="login"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^logout/$', views.logout, name="logout"),
    #url(r''  , views.hey, name="hey"),
]
