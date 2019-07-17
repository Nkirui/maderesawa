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
    re_path(r'^create/$', employer.drivercreate, name='drivercreate'),
    re_path(r'^view/(?P<pk>\d+)/$', employer.driverview, name='driverview'),
    re_path(r'^edit/(?P<pk>\d+)/$', employer.driveredit, name='driveredit'),
    re_path(r'^remove/(?P<pk>\d+)/$', employer.driverremove, name='driverremove'),
    re_path(r'^company/$', employer.saccoprofdisp, name='saccoprofdisp'),
    re_path(r'^staff/$', employer.createstaff, name='createstaff'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        employer.activate, name='activate'),

]