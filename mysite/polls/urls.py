from django.conf.urls import url, patterns

from polls import views

urlpatterns= [ url(r'^$', views.index, name='index'),
               url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
               url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
               url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

               ]
               
