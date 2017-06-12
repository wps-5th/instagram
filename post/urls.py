from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^$', views.post_list, name='list'),
    url(r'^create/$', views.post_create, name='create'),
    url(r'^(?P<post_pk>\d+)/modify/$', views.post_modify, name='modify'),
    url(r'^(?P<post_pk>\d+)/$', views.post_detail, name ='detail'),
]