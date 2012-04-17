from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'petstore.views.home', name='home'),
    # url(r'^petstore/', include('petstore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # django admin:
    url(r'^admin/', include(admin.site.urls)),
)

if not settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve', {'document_root':settings.STATIC_ROOT, 'insecure':True} ),
        url(r'^media/(?P<path>.*)$', 'serve', {'document_root':settings.MEDIA_ROOT, 'insecure':True} ),
    )

