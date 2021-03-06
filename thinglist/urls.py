from django.conf.urls import patterns, url

from thinglist import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^add/category/$', views.addCategory, name='addC'),
  url(r'^(?P<category_name>[^/]+)/$', views.category, name='category'),
  url(r'^(?P<category_name>[^/]+)/add/item/$', views.addItem, name='addI'),
  url(r'^(?P<category_name>[^/]+)/(?P<item_name>[^/]+)/$', views.item, name='item'),
  url(r'^(?P<category_name>[^/]+)/(?P<item_name>[^/]+)/add/note/$', views.addNote, name='addN'),
  url(r'^(?P<category_name>[^/]+)/(?P<item_name>[^/]+)/(?P<note_id>\d+)/$', views.note, name='note'),
)
