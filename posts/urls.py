from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^music/$', views.music, name='music'),
    url(r'^contatti/$', views.contatti, name='contatti'),
    url(r'^guitar/$', views.guitar, name='guitar'),
    url(r'^news/$', views.news, name='news'),
    url(r'^login/$', views.login, name='login'),


]