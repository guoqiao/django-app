from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'nzpower.views.index', name='home'),
    url(r'^nzpower/', include('nzpower.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
