from django.conf.urls import *
from game import views

urlpatterns = patterns('',
    url('^$', views.index),
    url('^new/$', views.new),
    url('^(?P<id>\d)', views.resume),
)
