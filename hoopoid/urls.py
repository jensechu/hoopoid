from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView, DetailView, ListView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hoopoid.views.home', name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                    'document_root': settings.MEDIA_ROOT,
        }),
    )

urlpatterns += patterns('hoopoid.inventory.views', 
    #url(r'^(?P<slug>[\w_-]+)/', 'section', name="section"),
    url(r'^store', 'store', name="default"),
)

urlpatterns += patterns('hoopoid.content.views', 
    url(r'^(?P<slug>[\w_-]+)/', 'section', name="section"),
    url(r'^$', 'section', name="default"),
)
