from django.conf.urls import patterns, include, url

urlpatterns = patterns('micro_admin.views',

    url(r'^$', 'index', name='microadmin_index'),
    url(r'^login/$', 'user_login', name='login'),
    url(r'^users/$', 'userslist', name='userslist'),
    url(r'^groups/$', 'groupslist', name='groupslist'),
    url(r'^centers/$', 'centerslist', name='centerslist'),
    url(r'^createuser/$', 'createuser', name='createuser'),
    url(r'^createbranch/$', 'create_branch', name='createbranch'),
    url(r'^creategroup/$', 'create_group', name='creategroup'),
    url(r'^createclient/$','create_client', name='createclient'),
    url(r'^createcenter/$', 'create_center', name='createcenter'),
    url(r'^searchcenter/$', 'searchcenter', name='searchcenter'),
    url(r'^searchgroup/$', 'searchgroup', name='searchgroup'),
    url(r'^searchuser', 'searchuser', name='searchuser'),
    url(r'^logout/$', 'user_logout', name='logout'),
)