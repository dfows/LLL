from django.conf.urls import patterns, url

from thinglist import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<category_name>\w+)/$', views.category, name='category'),
  url(r'^(\w+)/(?P<item_name>(\w+\-?)+)/$', views.item, name='item'),
  url(r'^(\w+)/(\w+\-?)+/(?P<note_id>\d+)/$', views.note, name='note'),
)
