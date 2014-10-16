from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^microfinanceadmin/', include('micro_admin.urls', namespace='micro_admin')),

)
