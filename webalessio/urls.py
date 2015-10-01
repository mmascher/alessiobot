from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index_json$', views.index_json, name='index_json'),
    url(r'^set_presence/(?P<user_id>\d+)$', views.set_presence, name='set_presence'),
]
