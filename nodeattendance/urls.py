from django.conf.urls import patterns, include, url
from attendanceapp.views import *
from django.conf import settings
from nodeattendance import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', login),
	url(r'^enter_attendance/',enter_attendance),
    # Examples:
    # url(r'^nodeattendance/', include('nodeattendance.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
