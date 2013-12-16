from django.conf.urls import patterns, url

from thinglist import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<category_name>\d+)/$', views.category, name='categ'),
  #url(r'^(?P<category>\d+)/(?P<item_id>\d+)/$', views.item),
)
