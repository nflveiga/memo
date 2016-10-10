from django.conf.urls import url

from protocols import views

urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^(?P<protocol_id>\d+)/$', views.protocoldetail, name='protocoldetail'),
]

