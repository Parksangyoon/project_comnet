from django.conf.urls import url
from . import views


urlpatterns = [
  url(r'^$', views.goto_game),
  url(r'^Loading/$', views.goto_Loading),
  url(r'^HowtoGame/$', views.goto_HowtoGame),
  url(r'^Editor/$', views.goto_Editor),
  url(r'^Select_Character/(?P<playnum>.+)/$', views.goto_Select_Character),
  url(r'^SelectCard/(?P<locnum>.+)/$', views.goto_SelectCard),
  url(r'^characterloading/(?P<locnum>.+)/$', views.goto_cardend),
  url(r'^Select_Cardend/(?P<locnum>.+)/$', views.goto_selectend),
  url(r'^PlayScreen/(?P<locnum>.+)/$', views.goto_PlayScreen),
  url(r'^Loopplay/(?P<locnum>.+)/$', views.Loop_play)
]
