from django.conf.urls import url
from . import views

app_name = 'portfolio'

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^SexyDashboard/$', views.sexyDashboard, name='sexyDashboard'),
    url(r'^CatCareIoTSystem/$', views.cat, name='cat'),
    url(r'^HarryCane/$', views.cane, name='cane'),
    url(r'^WeatherBot/$', views.weather, name='weather'),
    url(r'^Maze/$', views.maze, name='maze'),
]