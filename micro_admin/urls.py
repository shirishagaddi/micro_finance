from django.conf.urls import patterns, include, url

urlpatterns = patterns('micro_admin.views',

    url(r'^$', 'base', name='microadmin_base'),
    url(r'^login/$', 'login', name='microadmin_login'),
    url(r'^createbranch/$', 'create_branch', name='microadmin_branch'),
    url(r'^createclient/$','create_client', name='microadmin_client'),
)