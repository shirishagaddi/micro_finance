from django.conf.urls import patterns, include, url

urlpatterns = patterns('micro_admin.views',

    url(r'^$', 'base', name='microadmin_base'),
    url(r'^login/$', 'login', name='microadmin_login'),
    url(r'^client_list/$','client_list',name='client_list'),
    url(r'^createbranch/$', 'create_branch', name='microadmin_branch'),
    url(r'^createclient/$','create_client', name='microadmin_client'),
    url(r'^updateclientprofile/(?P<client>\d+)/$','update_profile',name='updateclientprofile'),
    url(r'^deleteclientprofile/(?P<client>\d+)/$','deleteclient_profile',name='deleteclientprofile'),

)