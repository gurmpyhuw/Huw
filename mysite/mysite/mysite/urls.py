"""
Definition of urls for mysite.
"""

from django.conf.urls import patterns, include, url
from Contact.views import * 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.mysite.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #url(r'^$', home),
    #url(r'^hello/$', hello),
    #url(r'^time/$', current_datetime),
    #url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    #url(r'^search-form/$', search_form),
    #url(r'^search/$', search),
    #url(r'^contact/$', contact),
)
