from django.conf.urls import url, patterns
from menu import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^(?P<cafe_id>\d+)/$', views.detail, name='detail'),
    #url(r'^(?P<cafe_id>\d+)/vote/$', views.vote, name='vote'),
    #url(r'^(?P<cafe_id>\d+)/results/$', views.results, name='results'),
)
