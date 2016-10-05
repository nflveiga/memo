from django.conf.urls import url

from drugs import views

urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^(?P<drug_id>\d+)/$', views.drugdetail, name='drugdetail'),
     url(r'^perf_calc/', views.perf_calc, name='perf_calc'),

]
