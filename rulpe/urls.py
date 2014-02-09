from django.conf.urls import patterns, url
import sys
import os

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


sys.stderr.write(os.path.join(os.path.dirname(__file__), '../', 'static').replace('\\', '/'))
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'rulpe.apps.shortener.views.home', name='home'),
    url(r'^shortener/$', 'rulpe.apps.shortener.views.shortener', name='shortener'),
    url(r'^(?P<shorten>\w+)/$', 'rulpe.apps.shortener.views.counter', name='counter'),
    # url(r'^rulpe/', include('rulpe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^favicon\.ico$', 'django.views.generic.simple.red1irect_to', {'url': os.path.join(os.path.dirname(__file__), '..//', 'static').replace('\\', '/')+'/img/favicon.ico'}),
)