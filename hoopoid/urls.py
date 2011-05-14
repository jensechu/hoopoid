from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView, DetailView, ListView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hoopoid.views.home', name='home'),
    
    url(r'^store.html', 'inventory.views.store'), 

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic.simple',
    url(r'^$', 'direct_to_template', {'template': 'home.html'}),
    url(r'^(?P<template>[\w_-]+.html)/?$', 'direct_to_template', name="page"),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                    'document_root': settings.MEDIA_ROOT,
        }),
    )
