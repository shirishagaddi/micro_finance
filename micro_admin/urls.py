from django.conf.urls import patterns, include, url

urlpatterns = patterns('micro_admin.views',

    url(r'^$', 'index', name='microadmin_index'),
    url(r'^login/$', 'user_login', name='login'),
    url(r'^users/$', 'userslist', name='userslist'),
    url(r'^createuser/$', 'createuser', name='createuser'),
    url(r'^client_list/$','client_list',name='client_list'),
    url(r'^clientprofile/(?P<client>\d+)/$', 'clientprofile', name='clientprofile'),
    url(r'^branch_list/$','branch_list',name='branch_list'),
    url(r'^createbranch/$', 'create_branch', name='createbranch'),
    url(r'^creategroup/$', 'create_group', name='creategroup'),
    url(r'^createclient/$','create_client', name='createclient'),
    url(r'^updateclientprofile/(?P<client>\d+)/$','update_profile',name='updateclientprofile'),
    url(r'^deleteclientprofile/(?P<client>\d+)/$','deleteclient_profile',name='deleteclientprofile'),
    url(r'^logout/$', 'user_logout', name='logout'),

)