from django.conf.urls import *
from game import views

urlpatterns = patterns('',
    url('^$', views.index),
)
