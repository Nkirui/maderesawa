from django.urls import path, re_path

from .views import msacco,employer,driver

urlpatterns = [

    #msacco
    path('',msacco.home, name='home'),

    #driver
    re_path(r'^search/$', driver.search, name='search'),
    re_path(r'^result/$', driver.getProfile, name='getProfile'),

    #Employer
    re_path(r'^list/$', employer.driverlist, name='driverlist'),
    re_path(r'^create/$', employer.drivercreate, name='drivercreate')




]