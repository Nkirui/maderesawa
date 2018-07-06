from django.urls import path, re_path
from .views import msacco,driver



urlpatterns = [
    path('',msacco.home, name='home'),
    re_path(r'^search/$', msacco.search, name='search'),
    #re_path(r'^result/(?P<dl>[-\w]+)/$', msacco.getProfile, name='getProfile'),
    re_path(r'^result/$', msacco.getProfile, name='getProfile'),

]