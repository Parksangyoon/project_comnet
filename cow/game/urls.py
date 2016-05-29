from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),  #기본접속시 
	url(r'^selectcharacter/', views.selectcharacter),
	url(r'^selectcard/', views.selectcard)
]
