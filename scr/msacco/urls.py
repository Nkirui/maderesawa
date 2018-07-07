from django.urls import path, re_path

from .views import msacco,employer,driver

urlpatterns = [
    path('',msacco.home, name='home'),
    re_path(r'^search/$', driver.search, name='search'),
    re_path(r'^list/$', employer.deriverlist, name='deriverlist'),
    #re_path(r'^result/(?P<dl>[-\w]+)/$', msacco.getProfile, name='getProfile'),
    re_path(r'^result/$', driver.getProfile, name='getProfile'),


]