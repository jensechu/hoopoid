from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView, DetailView, ListView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hoopoid.views.home', name='home'),
    url(r'^(?P<slug>[\w_-]+)/', 'hoopoid.content.views.section', name="section"),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
                       
    url(r'^$', 'hoopoid.content.views.section', name="default"),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                    'document_root': settings.MEDIA_ROOT,
        }),
    )
